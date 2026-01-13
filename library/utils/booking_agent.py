import re
import json
from dotenv import load_dotenv
from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from .booking_tools import get_price
from .service_context import build_service_context

load_dotenv()

# ------------------------------------------------------------------
# STATE
# ------------------------------------------------------------------

class ChatState(TypedDict):
    messages: list
    selected_code: str | None
    quantity: int | None


# ------------------------------------------------------------------
# LLM
# ------------------------------------------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

SERVICE_CONTEXT = build_service_context()
print("service context: ", SERVICE_CONTEXT)
SYSTEM_PROMPT = f"""
You are a friendly household electrician booking assistant.

Your responsibilities:
- Understand user problems in natural language
- Select the most relevant service from the catalog
- Never expose service codes to the user
- Ask only for missing info (quantity)
- Be polite, concise, and helpful

Service Catalog:
{SERVICE_CONTEXT}

Rules:
- Do NOT invent services
- If multiple services match, ask a clarification question
- Pricing must come ONLY from tools
"""

# ------------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------------

def extract_quantity(text: str) -> int | None:
    match = re.search(r"\b(\d+)\b", text)
    return int(match.group(1)) if match else None


def last_human_message(messages):
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            return msg.content
    return ""


# ------------------------------------------------------------------
# NODES
# ------------------------------------------------------------------

def llm_node(state: ChatState):
    if not state["messages"]:
        state["messages"].append(SystemMessage(content=SYSTEM_PROMPT))

    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    return state


def select_service_node(state: ChatState):
    user_text = last_human_message(state["messages"])

    prompt = f"""
User message:
"{user_text}"

From the service catalog, identify the best matching service.

Return STRICT JSON only in this format:
{{
  "service_code": "FAN_REPAIR",
  "confidence": "high"
}}

If unclear, return:
"NEED_CLARIFICATION"
"""

    response = llm.invoke(
        state["messages"] + [AIMessage(content=prompt)]
    )

    try:
        data = json.loads(response.content)
    except Exception:
        state["messages"].append(
            AIMessage(content="Could you please explain the issue a bit more?")
        )
        return state

    if data == "NEED_CLARIFICATION":
        state["messages"].append(
            AIMessage(content="Can you tell me what exactly is wrong?")
        )
        return state

    state["selected_code"] = data["service_code"]

    readable_name = data["service_code"].replace("_", " ").title()

    state["messages"].append(
        AIMessage(
            content=f"Got it 👍 You need **{readable_name}**.\nHow many units?"
        )
    )
    return state


def quantity_handler_node(state: ChatState):
    user_text = last_human_message(state["messages"])

    qty = extract_quantity(user_text) or 1
    state["quantity"] = qty

    result = get_price.invoke({
        "code": state["selected_code"],
        "quantity": qty
    })

    state["messages"].append(
        AIMessage(
            content=(
                f"💰 **Price Details**\n"
                f"Service: {result['name']}\n"
                f"Quantity: {qty}\n"
                f"Total (base price): ₹{result['total_price']}\n"
                f"(Taxes & visit charges not included)"
            )
        )
    )

    return state


# ------------------------------------------------------------------
# ROUTER
# ------------------------------------------------------------------

def router(state: ChatState):
    if not state.get("selected_code"):
        return "select_service"

    if state.get("selected_code") and not state.get("quantity"):
        return "quantity_handler"

    return END


# ------------------------------------------------------------------
# GRAPH
# ------------------------------------------------------------------

def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("llm", llm_node)
    graph.add_node("select_service", select_service_node)
    graph.add_node("quantity_handler", quantity_handler_node)

    graph.set_entry_point("llm")

    graph.add_conditional_edges(
        "llm",
        router,
        {
            "select_service": "select_service",
            "quantity_handler": "quantity_handler",
            END: END
        }
    )

    graph.add_edge("select_service", END)
    graph.add_edge("quantity_handler", END)

    return graph.compile()
