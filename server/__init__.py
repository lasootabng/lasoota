from fastapi import APIRouter, Depends
from . import login, org, user, services # , landing, conversation
from src.middleware import authentication

basic_router = APIRouter()

# dependencies added to decode token
api_router = APIRouter(dependencies=[Depends(authentication)])

# These router don't need tokens
basic_router.include_router(login.router, tags=["Login"])
# basic_router.include_router(conversation.router)

# API router with tokens
api_router.include_router(org.router, prefix="/org", tags=['Organization'])
api_router.include_router(user.router, tags=["User"])
api_router.include_router(services.router, tags=["Services"])
# api_router.include_router(landing.router, tags=["Landing"])

