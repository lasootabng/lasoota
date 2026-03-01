import shortuuid
from fastapi import APIRouter, Request, HTTPException # WebSocket
from src.logger import logger
from src.data_model import OrderSupportRequest
from library.db import (session_scope, Order, UserAddress as UA, SupportConversation as SC, receive_query)

router = APIRouter()


@router.post("/order-support")
def support(request: Request, chat: OrderSupportRequest):
    try:
        context = request.state.context
        logger.info(context)
        logger.info(chat)

        msg_id = shortuuid.ShortUUID().random(length=6).upper()
        with session_scope() as session:
            if not chat.conversation_id:
                conver_id = shortuuid.ShortUUID().random(length=8).upper()
                order_details = receive_query(session.query(
                    Order.id.label("booking_id"),  Order.scheduled_date.label("booking_date"),
                    Order.total_amount
                    ).filter(Order.user_id == context['user']['user_id'],
                            Order.is_active == True).all())
                
                # Add conversation in db
                # query = SC(
                #     conversation_id=conver_id,
                #     topic=chat.topic,
                #     label=chat.label
                # )
                # session.add(query)
                # session.commit()
            
                logger.info(f"order details: \n{order_details}")
                
                return {
                    "ok": True,
                    "conversation_id": conver_id,
                    "message_id": msg_id,
                    "status": "queued",
                    "created_at": "2026-03-01T13:10:00.150Z",
                    "next_step": "chat" if len(order_details) == 1 else "select_booking",
                    "booking_list": order_details
                }
            else:
                reply_id = shortuuid.ShortUUID().random(length=6).upper()
                return {
                        "ok": True,
                        "conversation_id": chat.conversation_id,
                        "message_id": msg_id,
                        "status": "queued",
                        "created_at": "2026-03-01T12:35:01.120Z",
                        "agent": {
                            "id": "agent_1",
                            "name": "Support Team"
                        },
                        "reply": {
                            "id": reply_id,
                            "type": "text",
                            "text": "Our support team will call you in a few minutes. Thanks for your patience.",
                            "created_at": "2026-03-01T12:35:01.130Z"
                        },
                        "next_step": "chat",
                        "booking_list": []
                    }
            
                    # if error:
                    #     return {
                    #         "ok": False,
                    #         "error": {
                    #             "code": "INVALID_BOOKING_ID",
                    #             "message": "Booking ID is invalid for this user."
                    #         }
                    #     }


    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")
    
# Request body
# {
#   "conversation_id": null,
#   "message_id": "usr_01",
#   "topic": "cancel_booking",
#   "label": "Cancel Booking",
#   "booking_id": null,
#   "source": "app_support_booking_help",
#   "message": {
#     "type": "text",
#     "text": "Hi, I need help to cancel my booking."
#   },
#   "meta": {
#     "platform": "android",
#     "app_section": "support_tab"
#   },
#   "sent_at": "2026-03-01T13:10:00.000Z"
# }


# @router.websocket("/ws/chat")
# async def chat(ws: WebSocket):
#     await ws.accept()

#     state = {
#         "messages": [],
#         "selected_code": None
#     }

#     await ws.send_text("Hi 👋 What electrician service do you need?")

#     while True:
#         user_msg = await ws.receive_text()
#         print("user message", user_msg)
#         await ws.send_text("I'm here to help you with your electrician needs.")
