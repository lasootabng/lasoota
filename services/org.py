from typing import Annotated
from fastapi import APIRouter, Request, Body
from src.data_model import ContactUS
from src.logger import logger
from src.constants import response_formatter

router = APIRouter()


@router.post("/contact-us")
def contact_us(request: Request, data: Annotated[ContactUS, Body(embed=True)]):
    context = request.state.context
    user_id = context['phone']
    logger.info(f"user request: {user_id} - comment: {data.comment}")
    return response_formatter(data={"message": "we will contact you soon!"})