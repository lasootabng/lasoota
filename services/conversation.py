from fastapi import APIRouter, WebSocket
from langchain.messages import HumanMessage
from library.utils.booking_agent import build_graph

router = APIRouter()
graph = build_graph()

@router.websocket("/ws/chat")
async def chat(ws: WebSocket):
    await ws.accept()

    state = {
        "messages": [],
        "selected_code": None
    }

    await ws.send_text("Hi 👋 What electrician service do you need?")

    while True:
        user_msg = await ws.receive_text()
        print("user message", user_msg)

        state["messages"].append(
            HumanMessage(content=user_msg)
        )

        state = graph.invoke(state)

        last_reply = state["messages"][-1].content
        await ws.send_text(last_reply)
