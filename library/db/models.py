from sqlalchemy import (Column, Integer, String, Boolean, Float,  Numeric,
                         DateTime, UniqueConstraint, TIMESTAMP, ForeignKey,
                           CheckConstraint, func)
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


class Catalog(Base):
    __tablename__ = "catalog"

    id = Column(Integer, primary_key=True, index=True)
    catalog_name = Column(String(255), nullable=False)
    visit_fee = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    created_on = Column(TIMESTAMP, server_default=func.now())
    updated_on = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # 🔗 Relationships
    category = relationship(
        "Category",
        back_populates="catalog",
        cascade="all, delete",
        passive_deletes=True
    )



class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    catalog_id = Column(Integer, ForeignKey("catalog.id", ondelete="CASCADE"), nullable=False)
    category_name = Column(String(100), nullable=False)
    icon = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # 🔗 Relationships
    catalog = relationship(
        "Catalog",
        back_populates="category"
    )

    services = relationship(
        "Services",
        back_populates="category",
        cascade="all, delete",
        passive_deletes=True
    )

    __table_args__ = (
        UniqueConstraint(
            "catalog_id",
            "category_name",
            name="unique_subcategory_per_service"
        ),
    )

class Services(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(150), nullable=False)
    price_min = Column(Numeric(10, 2), nullable=False)
    price_max = Column(Numeric(10, 2), nullable=True)
    pricing_note = Column(String(250), nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    rating = Column(Numeric(2, 1), nullable=True)
    review_count = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # 🔗 Relationships
    category = relationship(
        "Category",
        back_populates="services"
    )

    __table_args__ = (
        CheckConstraint(
            "price_min >= 0",
            name="services_price_check"
        ),
        CheckConstraint(
            "rating IS NULL OR rating BETWEEN 0 AND 5",
            name="services_rating_check"
        ),
        CheckConstraint(
            "review_count >= 0",
            name="services_review_count_check"
        ),
        CheckConstraint(
            "duration_minutes IS NULL OR duration_minutes > 0",
            name="services_duration_minutes_check"
        ),
    )