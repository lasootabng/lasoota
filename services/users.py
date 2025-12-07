from json import dumps
from typing import Literal
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, constr
from library.otp.otp import generate_otp
from library.gmail.mail import mail_otp
from library.cache.cache import get_pending_signup, save_pending_signup

router = APIRouter()


class User(BaseModel):
    full_name: str
    email: EmailStr
    phone: constr(min_length=10, max_length=13)  # type: ignore
    role: Literal["Provider", "Customer"]

# register
@router.post("/register", tags=["Register User"])
async def register_user(user: User):
    otp, otp_timeout = generate_otp()
    # save otp and user info
    save_pending_signup(
        user.phone,
        dumps({
            "otp": otp,
            "otp_timeout": otp_timeout,
            "user_info": {
                "full_name": user.full_name,
                "email": user.email,
                "phone": user.phone,
                "role": user.role
            }
        })
    )
    print(f"OTP: {otp}")
    # sending otp to user
    # mail_otp(user.email, otp, "Bipul")
    return user