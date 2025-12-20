""" middleware.py"""

import jwt
from typing import Annotated
from fastapi import Request, Header, HTTPException #, Depends
# from fastapi.security import OAuth2PasswordBearer
from src.logger import logger


SECRET_KEY = "e1f6a9c3b7d2e5f8a1c9d4e7b6a2f9c1d3e5a7b8c9d0f2a6b4c8d9e3f7a2b5c"
ALGORITHM = "HS256"

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def token_decoder(token):
    """ Token Decoder """
    logger.info("decoding token")
    context = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    logger.info(context)
    return context


# def authentication(token: Annotated[str, Depends(oauth2_scheme)], request: Request):
def authentication(token: Annotated[str, Header()], request: Request):
    """ Authentication Middleware """
    try:
        token = token.split()
        request.state.context = token_decoder(token[1])
        logger.info(f"Token decoded! {request.state.context}")
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=400, detail={
            "data": "Please provide valid token!",
            "error": True
        })