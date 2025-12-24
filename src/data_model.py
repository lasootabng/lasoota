from pydantic import BaseModel, EmailStr, constr
from typing import Literal

class UpdateUser(BaseModel):
    full_name: str
    email: EmailStr

class userLogin(BaseModel):
    phone: constr(min_length=10, max_length=13)  # type: ignore
    role: Literal["Provider", "Customer"]

class ValidOTP(BaseModel):
    otp: int
    phone: constr(min_length=10, max_length=13)  # type: ignore
    # new_login: bool

class Token(BaseModel):
    access_token: str
    phone: constr(min_length=10, max_length=13)  # type: ignore

class ContactUS(BaseModel):
    comment: str

class UserAddress(BaseModel):
    full_name: str
    house: str
    area: str
    landmark: str
    pincode: constr(min_length=6, max_length=6) # type: ignore
    mobile: constr(min_length=10, max_length=13) # type: ignore

class RemoveAddress(BaseModel):
    address_id: int

class UpdateAddress(BaseModel):
    user_address: UserAddress
    remove_address: RemoveAddress
