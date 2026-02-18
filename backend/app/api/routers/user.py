from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dp import get_db
from app.services.user import UserService
from fastapi import HTTPException, status
from app.schemas.user import UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@router.post("/register")
async def registetr(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    user = await user_service.create_user(user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )
    return user
