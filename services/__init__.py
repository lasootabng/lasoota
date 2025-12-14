from fastapi import APIRouter, Depends
from . import users, org
from src.middleware import authentication

basic_router = APIRouter()

# dependencies added to decode token
api_router = APIRouter(dependencies=[Depends(authentication)])

# These router don't need tokens
basic_router.include_router(users.router, tags=["Users"])

# API router with tokens
api_router.include_router(org.router, prefix="/org", tags=['Organization'])

