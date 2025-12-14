import jwt
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter
from library.otp.otp import generate_otp
from library.gmail.mail import mail_otp
from library.cache.cache import get_pending_signup, save_pending_signup, delete_pending_signup
from library.db import session_scope, Users
from src.logger import logger
from src.constants import response_formatter
from src.data_model import UserReg, userLogin, ValidOTP, Token

router = APIRouter()


SECRET_KEY = "e1f6a9c3b7d2e5f8a1c9d4e7b6a2f9c1d3e5a7b8c9d0f2a6b4c8d9e3f7a2b5c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300




def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/register")
async def register_user(user_reg: UserReg):
    # check user phone is already registered or not
    with session_scope() as session:
        users_data = session.query(Users.full_name, Users.email, Users.phone_number).filter(Users.phone_number == user_reg.phone).all()
        logger.info(f"users Data: {users_data}")
        
        if users_data:
            return response_formatter({"status": "user already exists"})
        
        query = Users(
            email = user_reg.email,
            phone_number=user_reg.phone,
            full_name=user_reg.full_name,
            role_type=user_reg.role,
            is_verified=False,
            password_hash = "sample"
        )
        session.add(query)
        session.commit()
        logger.info("User created!")

    otp, otp_timeout = generate_otp()

    # save otp and user info to redis
    save_pending_signup(
        user_reg.phone,
        {
            "otp": otp,
            "otp_timeout": str(otp_timeout),
        }
    )
    
    logger.info(f"OTP: {otp}")
    # sending otp to user
    # mail_otp(user.email, otp, "Bipul")
    return user_reg


@router.post("/validate-otp")
def validate_otp(otp_val: ValidOTP):
    logger.info(otp_val)
    # otp_data = get_pending_signup(otp_val.phone)
    # if otp_data["otp"]== otp_val.otp:
    if 1234 == otp_val.otp:
        logger.info("OTP verified")
        if otp_val.new_login:
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
        access_token = create_access_token(
            data={"sub": "Bipulsingh", "phone": otp_val.phone}, expires_delta=access_token_expires
        )
        logger.info("Return response")
        return response_formatter(Token(access_token=access_token, token_type="bearer", phone=otp_val.phone))
    else:
        logger.info("invalid OTP")
    return response_formatter({
        "success": False})

@router.post("/login")
def login_user(user_login: userLogin):

    with session_scope() as session:
        users_data = session.query(Users.full_name, Users.email, Users.phone_number).filter(Users.phone_number == user_login.phone).all()
        logger.info(f"users Data: {users_data}")
        
    if not users_data:
        return response_formatter({"status": "please register user first"})
    
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
    return {"success": True}

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
        return response_formatter({"status": "OTP is sent to register mobile number."})
    except Exception as ex:
        logger.exception(ex)
        return response_formatter(data={"success": False}, status_code=500)
