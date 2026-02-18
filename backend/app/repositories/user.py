from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from typing import Optional
from sqlalchemy import select
from app.schemas.user import UserCreate
import hashlib


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_for_id(
        self,
        user_id: int
    ) -> Optional[User]:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_user_for_email(
        self,
        email: str
    ) -> Optional[User]:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create_user(
        self,
        user_data: UserCreate
    ) -> Optional[User]:

        hash_pass = hashlib.sha256(user_data.password.encode()).hexdigest()

        user_dict = user_data.model_dump()
        user_dict["hash_password"] = hash_pass
        user_dict.pop('password', None)
        user_dict.pop('retry_password', None)
        user = User(**user_dict)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
