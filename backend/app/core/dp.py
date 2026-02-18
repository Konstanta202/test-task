from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from typing import AsyncGenerator


async_engine = create_async_engine(
    settings.DATABASE_URL_asyncpg,
    echo=True
)

AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error database: {str(e)}]"
            )
        except HTTPException:
            await session.rollback()
            raise
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error exception: {str(e)}]"
            )
        finally:
            await session.close()
