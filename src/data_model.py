from pydantic import BaseModel, EmailStr, constr, Field, field_validator, validator
from typing import Literal, Optional, List, TypedDict
from enum import Enum
from datetime import date
from decimal import Decimal

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

class RefreshToken(BaseModel):
    refresh_token: str

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

class SlotType(str, Enum):
    INSTANT = "instant"
    LATER = "later"

class ServiceItem(BaseModel):
    service_id: int  # Matching your SERIAL type from the DB
    quantity: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    services: List[ServiceItem]
    address_id: int
    slot_type: SlotType
    
    # Optional fields for 'later' bookings
    scheduled_date: Optional[date] = None
    scheduled_time: Optional[str] = None
    
    tip_amount: Decimal = Field(default=Decimal("0.00"))
    total_amount: Decimal
    payment_method: str = "cash"

    # @field_validator('scheduled_date', 'scheduled_time')
    # @classmethod
    # def check_later_fields(cls, v, info):
    #     # Logic: If slot_type is 'later', date/time should ideally not be null
    #     if info.data.get('slot_type') == SlotType.LATER and v is None:
    #         raise ValueError(f'{info.field_name} is required when slot_type is later')
    #     return v

