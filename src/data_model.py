from pydantic import BaseModel, EmailStr, constr
from typing import Literal

class UserReg(BaseModel):
    full_name: str
    email: EmailStr
    phone: constr(min_length=10, max_length=13)  # type: ignore
    role: Literal["Provider", "Customer"]

class userLogin(BaseModel):
    phone: constr(min_length=10, max_length=13)  # type: ignore

class ValidOTP(BaseModel):
    otp: int
    phone: constr(min_length=10, max_length=13)  # type: ignore
    new_login: bool

class Token(BaseModel):
    access_token: str
    token_type: str