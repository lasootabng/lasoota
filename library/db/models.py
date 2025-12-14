from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import ENUM

Base = declarative_base()

# Define ENUM type for role
user_role_enum = ENUM('Provider', 'Customer', name='user_role', create_type=True)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone_number = Column(String(20), nullable=True)
    full_name = Column(String(255), nullable=True)
    password_hash = Column(String(255), nullable=False)
    role_type = Column(user_role_enum, nullable=False, default='Customer')
    is_verified = Column(Boolean, nullable=False, default=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), server_default=func.now())