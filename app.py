from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, constr
from library.otp.otp import generate_otp
from library.gmail.mail import mail_otp

app =FastAPI()


class User(BaseModel):
    full_name: str
    email: EmailStr
    phone: constr(min_length=10, max_length=13)  # type: ignore
    role: Literal["Provider", "Customer"]

@app.get("/", tags=["health"])
async def health():
    return {"status": "ok", "message": "Bihar services API is running!"}


# register
@app.post("/register", tags=["Register User"])
async def register_user(user: User):
    otp = generate_otp()
    print(otp)
    mail_otp('kumarbipulsingh@gmail.com', otp, "Bipul")
    return user
