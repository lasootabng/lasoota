from pydantic import BaseModel, EmailStr, constr, validator
from typing import Literal, Optional, List, TypedDict

class UpdateUser(BaseModel):
    full_name: str
    email: Optional[EmailStr] = None
    # phone: constr(min_length=10, max_length=13)  # type: ignore

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
    latitude: float
    longitude: float
    flat: str
    society: Optional[str]
    landmark: Optional[str]
    city: str
    state: str
    pincode: str
    phone: Optional[str]


class RemoveAddress(BaseModel):
    address_id: int

class UpdateAddress(BaseModel):
    address_id: int
    flat: str
    society: Optional[str]
    landmark: Optional[str]
    phone: Optional[str]

class CartItem(BaseModel):
    code: str
    quantity: int
