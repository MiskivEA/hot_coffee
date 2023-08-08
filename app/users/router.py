from fastapi import APIRouter, Depends
from sqlalchemy import select, text, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.users.models import User, Follow
from .auth import fastapi_users

current_user = fastapi_users.current_user
user_router = APIRouter()


@user_router.post('/users/{user_id}/subscribe')
async def subscribe(user_id: int, user: User = Depends(current_user()),
                    session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.id == user_id)
    idol = await session.scalar(stmt)
    follow = Follow(
        follower=user.id,
        idol=idol.id
    )
    session.add(follow)
    await session.commit()
    return follow


