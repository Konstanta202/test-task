from pydantic import BaseModel, ConfigDict, EmailStr
from enum import Enum
from datetime import datetime


class UserRole(str, Enum):
    admin = "admin"
    moderator = "moderator"
    user = "user"


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    role: UserRole = UserRole.user
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    retry_password: str
