from typing import Optional, List
from sqlalchemy import String, Boolean, Enum, TIMESTAMP, BigInteger
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
import enum
from app.core.base import Base
from pydantic import EmailStr


class UserRole(enum.Enum):
    admin = "admin"
    moderator = "moderator"
    user = "user"


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        nullable=False
    )
    email: Mapped[EmailStr] = mapped_column(
        EmailStr,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    hash_password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    role: Mapped[UserRole] = mapped_column(
        Enum[UserRole],
        default=UserRole.user
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        server_default=func.now()
    )
    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )
