import re
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain.messages import AIMessage
from .booking_tools import search_service, get_price
from typing import TypedDict
from .service_context import build_service_context

load_dotenv()


class ChatState(TypedDict):
    messages: list
    selected_code: str | None
    quantity: int | None


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)


SERVICE_CONTEXT = build_service_context()

SYSTEM_PROMPT = f"""
You are a friendly household electrician booking assistant.

Your job:
- Understand the user's problem in natural language
- Identify the MOST RELEVANT service from the catalog below
- Internally select the correct service code
- NEVER ask the user for service codes
- Ask only for missing information (quantity, confirmation)
- Be conversational and helpful

Service Catalog:
{SERVICE_CONTEXT}

Rules:
- Do NOT invent services
- If multiple services match, ask a clarification question
- Prices are handled by tools only
"""

def extract_quantity(text: str) -> int | None:
    match = re.search(r"\b(\d+)\b", text)
    return int(match.group(1)) if match else None

def llm_node(state: ChatState):
    response = llm.invoke(
        [AIMessage(content=SYSTEM_PROMPT)] + state["messages"]
    )
    state["messages"].append(response)
    return state

def tool_router(state: ChatState):
    if not state.get("selected_code"):
        return "select_service"

    if state.get("selected_code") and not state.get("quantity"):
        return "quantity_handler"

    return END

def search_service_node(state: ChatState):
    last_user_msg = next(
        msg.content for msg in reversed(state["messages"])
        if msg.type == "human"
    )

    result = search_service.invoke({"query": last_user_msg})

    state["messages"].append(
        AIMessage(
            content=(
                "Here are matching electrician services.\n"
                "Please confirm the service code:\n\n"
                f"{result}"
            )
        )
    )
    return state


def get_price_node(state: ChatState):
    last_user_msg = next(
        msg.content for msg in reversed(state["messages"])
        if msg.type == "human"
    )

    match = re.search(r"\b[A-Z_]{3,}\b", last_user_msg)
    if not match:
        state["messages"].append(
            AIMessage(content="Please confirm the service code.")
        )
        return state

    code = match.group()
    state["selected_code"] = code

    state["messages"].append(
        AIMessage(
            content="How many units do you need?"
        )
    )
    return state


def quantity_handler_node(state: ChatState):
    last_user_msg = next(
        msg.content for msg in reversed(state["messages"])
        if msg.type == "human"
    )

    qty = extract_quantity(last_user_msg) or 1
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


def select_service_node(state: ChatState):
    last_user_msg = next(
        msg.content for msg in reversed(state["messages"])
        if msg.type == "human"
    )

    prompt = f"""
        User message:
        "{last_user_msg}"

        From the service catalog, identify:
        - service_code
        - confidence (high / medium / low)

        If unclear, say "NEED_CLARIFICATION"
        Return JSON only.
        """

    response = llm.invoke(
        state["messages"] + [AIMessage(content=prompt)]
    )

    try:
        data = json.loads(response.content)
    except Exception:
        state["messages"].append(
            AIMessage(content="Could you please describe the issue a bit more?")
        )
        return state

    if data == "NEED_CLARIFICATION":
        state["messages"].append(
            AIMessage(content="Can you tell me what exactly is wrong with the fan?")
        )
        return state

    state["selected_code"] = data["service_code"]

    state["messages"].append(
        AIMessage(
            content=f"Got it 👍 You need **{data['service_code'].replace('_', ' ').title()}**.\nHow many units?"
        )
    )
    return state



def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("llm", llm_node)
    graph.add_node("search_service", search_service_node)
    graph.add_node("get_price", get_price_node)
    graph.add_node("quantity_handler", quantity_handler_node)

    graph.set_entry_point("llm")

    graph.add_conditional_edges(
        "llm",
        tool_router,
        {
            "search_service": "search_service",
            "get_price": "get_price",
            "quantity_handler": "quantity_handler",
            "llm": END
        }
    )

    graph.add_edge("search_service", END)
    graph.add_edge("get_price", END)
    graph.add_edge("quantity_handler", END)

    return graph.compile()
