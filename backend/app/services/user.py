from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user import UserRepository
from app.schemas.user import UserResponse, UserCreate
from typing import Optional
from fastapi import HTTPException, status
from app.core.security import get_password_hash

class UserService:
    def __init__(self, session: AsyncSession):
        self.user_rep = UserRepository(session)

    async def get_user(
        self,
        user_id
    ) -> Optional[UserResponse]:
        user = await self.user_rep.get_user_for_id(
            user_id
        )
        if not user:
            return None
        return UserResponse.model_validate(user)

    async def create_user(
        self,
        user_data: UserCreate
    ) -> Optional[UserResponse]:
        exists = await self.user_rep.get_user_for_email(
            user_data.email
        )
        if exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists"
            )
        hash_password = get_password_hash(user_data.password)
        user_data.password = hash_password

        user = await self.user_rep.create_user(user_data)
        if not user:
            return None
        return UserResponse.model_validate(user)

    async def login_user(
        self,
        email: str,
        password: str
    ) -> Optional[UserResponse]:
        exists_user = self.user_rep.get_user_for_email(email)
        if not exists_user:
            return None
