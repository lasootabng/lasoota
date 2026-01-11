import jwt
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from library.utils.otp import generate_otp
from library.cache.cache import get_pending_signup, save_pending_signup, delete_pending_signup
from library.db import session_scope, Users
from src.logger import logger
from src.data_model import userLogin, ValidOTP, Token
import uuid

router = APIRouter()


SECRET_KEY = "e1f6a9c3b7d2e5f8a1c9d4e7b6a2f9c1d3e5a7b8c9d0f2a6b4c8d9e3f7a2b5c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000
REFRESH_TOKEN_EXPIRE = 7



def create_access_token(data: dict, expiry: timedelta | None = None, refresh: bool=False):
    payload = {}
    # to_encode = data.copy()
    payload['user' ] = data
    payload['exp'] = datetime.now(timezone.utc) + (
        expiry if expiry is not None else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    payload['jti'] = str(uuid.uuid4())
    payload['refresh'] = refresh

    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
    return token


@router.post("/validate-otp")
def validate_otp(otp_val: ValidOTP):
    logger.info(otp_val)
    otp_data = get_pending_signup(otp_val.phone)
    if otp_data["otp"]== otp_val.otp:
    # if 1234 == otp_val.otp:
        logger.info("OTP verified")
        
        # get user details
        with session_scope() as session:
            user_data = session.query(Users.id, Users.is_active).filter(Users.phone_number == otp_val.phone).all()

        if not user_data[0].is_active:
            logger.info("user Verified!")
            with session_scope() as session:
                session.query(Users).filter(
                    Users.phone_number == otp_val.phone
                ).update({
                    "is_verified": True,
                    "updated_on": datetime.now()
                })
                session.commit()
        
        logger.info("Deleting OTP")
        delete_pending_signup(otp_val.phone)

        # send Access token
        logger.info("Generating Access Token")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        data={"sub": "Bipulsingh", "phone": otp_val.phone, "user_id": user_data[0].id}
        access_token = create_access_token(
            data=data
        )
        refresh_token = create_access_token(
            data=data,
            refresh=True,
            expiry=timedelta(days=REFRESH_TOKEN_EXPIRE)
        )
        logger.info("Return response")
        return Token(access_token=access_token, refresh_token=refresh_token, token_type= "bearer")
    else:
        logger.info("invalid OTP")
    return JSONResponse(content={"message": "invalid OTP"}, status_code=400)

@router.post("/login")
def login_user(user_login: userLogin):
    try:
        with session_scope() as session:
            users_data = session.query(Users.full_name, Users.email, Users.phone_number).filter(Users.phone_number == user_login.phone).all()
            logger.info(f"users Data: {users_data}")
            
            if not users_data:
                query = Users(
                phone_number=user_login.phone,
                role_type=user_login.role,
                is_verified=False)

                session.add(query)
                session.commit()
                logger.info("User created!")
        
        # Generate OTP for login
        otp, otp_timeout = generate_otp()
        
        # Save OTP in redisk
        save_pending_signup(
            user_login.phone,
            {
                "otp": otp,
                "otp_timeout": str(otp_timeout),
            }
        )
        logger.info("OTP saved")
        # sending otp to user
        # logger.info(f"user email: {users_data[0].ema/il}")
        # mail_otp(user.email, otp, "Bipul")
        return {"success": True}
    except Exception as ex:
        logger.exception(ex)
        HTTPException(status_code=500, detail="something went wrong")

@router.post("/resend-otp")
def resend_otp(user_login: userLogin):
    try:
         # Generate OTP for login
        otp, otp_timeout = generate_otp()
        
        # Save OTP in redisk
        save_pending_signup(
            user_login.phone,
            {
                "otp": otp,
                "otp_timeout": str(otp_timeout),
            }
        )
        logger.info("OTP saved")
        # sending otp to user
        # mail_otp(user.email, otp, "Bipul")
        return {"status": "OTP is sent to register mobile number."}
    except Exception as ex:
        logger.exception(ex)
        return JSONResponse(content={"success": False}, status_code=500)
