from pydantic import BaseModel, EmailStr, constr, validator
from typing import Literal, Optional, List, TypedDict

class UpdateUser(BaseModel):
    full_name: str
    email: Optional[EmailStr] = None
    phone: constr(min_length=10, max_length=13)  # type: ignore

    @validator("email", pre=True, always=True)
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v


class userLogin(BaseModel):
    phone: constr(min_length=10, max_length=13)  # type: ignore
    role: Literal["Provider", "Customer"]

class ValidOTP(BaseModel):
    otp: int
    phone: constr(min_length=10, max_length=13)  # type: ignore

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    # phone: constr(min_length=10, max_length=13)  # type: ignore

class ContactUS(BaseModel):
    comment: str

class UserAddress(BaseModel):
    full_name: str
    address1: str
    address2: str
    landmark: str
    pincode: constr(min_length=6, max_length=6) # type: ignore
    phone: constr(min_length=10, max_length=13) # type: ignore

class RemoveAddress(BaseModel):
    address_id: int

class UpdateAddress(BaseModel):
    address_id: int
    full_name: str
    address1: str
    address2: str
    landmark: str
    pincode: constr(min_length=6, max_length=6) # type: ignore
    phone: constr(min_length=10, max_length=13) # type: ignore


class CartItem(BaseModel):
    code: str
    quantity: int


# class BookingState(BaseModel):
#     service: str | None = None
#     service_code: str | None = None
#     quantity: int | None = None
#     schedule: str | None = None
#     location: str | None = None
#     notes: str | None = None

#     cart: list = []
#     confirmed: bool = False
#     estimate: dict | None = None

#     user_message: str | None = None   # 👈 ADD THIS
#     last_bot_message: str | None = None

class ChatState(TypedDict):
    messages: List
    selected_code: Optional[str]