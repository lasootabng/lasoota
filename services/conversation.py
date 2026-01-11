import os
import re
import json
from dotenv import load_dotenv
from fastapi import WebSocket, APIRouter
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

from library.utils.tools import (
    search_service,
    get_price,
    estimate_cart
)

router = APIRouter()
load_dotenv()

# ----------------------------
# LLM
# ----------------------------

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

llm_with_tools = llm.bind_tools([
    search_service,
    get_price
])

# ----------------------------
# Helpers
# ----------------------------

def next_missing_field(state: dict):
    if not state.get("service"):
        return "service"
    if not state.get("schedule"):
        return "schedule"
    if not state.get("location"):
        return "location"
    return None


def build_prompt(state: dict, user_message: str):
    missing = next_missing_field(state)

    return f"""
    You are an AI service booking assistant for a household services app.

    Your job is to help the user book services step-by-step.

    =====================
    STRICT RULES
    =====================
    - Ask ONLY for the missing field shown below
    - Ask ONE question at a time
    - NEVER calculate prices yourself
    - NEVER assume or guess missing values
    - Be short, clear, and polite
    - Do NOT repeat information already present in the state
    - Do NOT move ahead unless the user confirms

    =====================
    TOOL USAGE RULES
    =====================
    - Use `search_service` ONLY when the user asks what services are available
    - Use `search_service` when the service is unclear or ambiguous
    - Use `get_price` ONLY when a service code and quantity are known
    - Do NOT call tools unless necessary
    - Do NOT call tools just to chat

    =====================
    CONVERSATION FLOW
    =====================
    1. Identify the service
    2. Identify the sub-service (service code)
    3. Ask for quantity
    4. Ask for schedule
    5. Ask for location
    6. Ask for confirmation before estimate

    =====================
    CURRENT STATE
    =====================
    {json.dumps(state, indent=2)}

    =====================
    USER MESSAGE
    =====================
    {user_message}

    =====================
    MISSING FIELD
    =====================
    {missing}

    =====================
    RESPONSE INSTRUCTIONS
    =====================
    - If a tool is required, CALL THE TOOL
    - Otherwise, respond with ONE natural language question
    - Do NOT include explanations or extra text
    """


# ----------------------------
# LangGraph Nodes
# ----------------------------

def agent_node(state: dict):
    response = llm_with_tools.invoke(
        build_prompt(state, state.get("user_message", ""))
    )
    return update_state_from_llm(state, response)


def cart_node(state: dict):
    cart = state.get("cart", [])

    cart.append({
        "code": state["service_code"],
        "quantity": state["quantity"]
    })

    state["cart"] = cart
    state.pop("service_code", None)
    state.pop("quantity", None)

    state["last_bot_message"] = (
        "Service added to cart. Would you like to add another service?"
    )
    return state


def confirm_node(state: dict):
    state["last_bot_message"] = (
        "I have all the details. Shall I generate the final estimate?"
    )
    return state


def estimate_node(state: dict):
    state["estimate"] = estimate_cart(state["cart"])
    state["last_bot_message"] = "Here is your final estimate."
    return state


# ----------------------------
# Routing Logic
# ----------------------------

def route(state: dict):
    # Add to cart
    if state.get("service_code") and state.get("quantity"):
        return "cart"

    # Ask for confirmation
    if state.get("cart") and not state.get("confirmed"):
        return "confirm"

    # Generate estimate
    if state.get("confirmed") and not state.get("estimate"):
        return "estimate"

    # ⛔ STOP after agent response
    return "end"

# ----------------------------
# Build LangGraph
# ----------------------------

graph = StateGraph(dict)

graph.add_node("agent", agent_node)
graph.add_node("cart", cart_node)
graph.add_node("confirm", confirm_node)
graph.add_node("estimate", estimate_node)

graph.set_entry_point("agent")

graph.add_conditional_edges(
    "agent",
    route,
    {
        "cart": "cart",
        "confirm": "confirm",
        "estimate": "estimate",
        "end": END        # 👈 MAP TO END
    }
)

graph.add_edge("cart", "agent")
graph.add_edge("confirm", "agent")
graph.add_edge("estimate", END)

booking_graph = graph.compile()

# ----------------------------
# State Update Logic
# ----------------------------

def update_state_from_llm(state: dict, response):
    # 🛠️ TOOL CALL HANDLING
    if response.tool_calls:
        for call in response.tool_calls:
            name = call["name"]
            args = call["args"]

            if name == "search_service":
                result = search_service(**args)
                state["last_bot_message"] = json.dumps(result, indent=2)

            elif name == "get_price":
                result = get_price(**args)
                state["last_bot_message"] = json.dumps(result, indent=2)

        return state


# ----------------------------
# WebSocket Endpoint
# ----------------------------

@router.websocket("/ws/chat")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    state = {
        "cart": [],
        "confirmed": False
    }

    while True:
        user_message = await ws.receive_text()   # 👈 TEXT, NOT JSON
        print("user message:", user_message)
        state["user_message"] = user_message

        state = booking_graph.invoke(state)

        await ws.send_json({
            "sender": "bot",
            "message": state.get("last_bot_message"),
            "quote": state.get("estimate"),
            "state": state
        })

