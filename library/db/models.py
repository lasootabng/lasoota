from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, func, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from geoalchemy2 import Geography


Base = declarative_base()

# Define ENUM type for role
user_role_enum = ENUM('Provider', 'Customer', name='user_role', create_type=True)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone_number = Column(String(20), nullable=True)
    full_name = Column(String(255), nullable=True)
    # password_hash = Column(String(255), nullable=False)
    role_type = Column(user_role_enum, nullable=False, default='Customer')
    is_verified = Column(Boolean, nullable=False, default=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)   # soft delete flag

    addresses = relationship(
        "UserAddress",
        back_populates="user",   # ✅ MUST match attribute name in UserAddress
        cascade="all, delete-orphan"
    )


class UserAddress(Base):
    __tablename__ = "user_address"

    address_id = Column(Integer, primary_key=True, index=True)

    # Foreign key
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Address details
    flat = Column(String(100), nullable=False)
    society = Column(String(150), nullable=True)
    landmark = Column(String(150), nullable=True)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    pincode = Column(String(10), nullable=False)

    phone = Column(String(15), nullable=True)

    # Coordinates
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # PostGIS geography column
    location = Column(Geography(geometry_type="POINT", srid=4326), nullable=False)

    # Metadata
    is_active = Column(Boolean, default=True)
    created_on = Column(TIMESTAMP, server_default=func.now())
    updated_on = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )

    # Optional relationship
    user = relationship("Users", back_populates="addresses")


class ServiceCategory(Base):
    __tablename__ = "service_category"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(255), nullable=False)
    category_order = Column(Integer, nullable=False)
    service_image = Column(String(500))
    created_on = Column(TIMESTAMP, server_default=func.now())
    updated_on = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)


class SubCategory(Base):
    __tablename__ = "sub_category"

    sub_category_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("service_category.category_id", ondelete="CASCADE"), nullable=False)
    sub_category_name = Column(String(255), nullable=False)
    sub_category_order = Column(Integer, nullable=False)
    sub_category_image = Column(String(500))
    created_on = Column(TIMESTAMP, server_default=func.now())
    updated_on = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)
