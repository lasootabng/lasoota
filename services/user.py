from fastapi import APIRouter, Request
from src.logger import logger
from src.constants import response_formatter
from library.db import session_scope, Users

router = APIRouter()

@router.get("/get-user")
def get_user(request: Request):
    try:
        context = request.state.context
        logger.info(f"user info: {context}")
        with session_scope() as session:
            user_data = session.query(Users.full_name, Users.email, Users.phone_number).filter(Users.phone_number == context['phone']).all()
        if user_data:
            user_data = user_data[0]
        else:
            return response_formatter(data={"message": "something wents wrong!"}, status_code=500)
        logger.info(f"users Data: {user_data}")
        user_info = {
                    "user": {"name": user_data.full_name,
                             "phone": user_data.phone_number,
                             },
                    "helplineNo": '7870743082'
                }
        return response_formatter(data=user_info)
    except Exception as ex:
        logger.exception(ex)

@router.get("/get-address")
def get_address(request: Request):
    try:
        context = request.state.context
        logger.info(context)
    except Exception as ex:
        logger.exception(ex)
