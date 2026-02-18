from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user import UserRepository
from app.schemas.user import UserResponse, UserCreate
from typing import Optional


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
    ) -> UserResponse:

        exists = await self.user_rep.get_user_for_email(
            user_data.email
        )
        if exists:
            return None

        user = await self.user_rep.create_user(user_data)
        if not user:
            return None
        return UserResponse.model_validate(user)
