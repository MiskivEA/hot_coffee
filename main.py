import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from app.database import create_db_and_tables
import asyncio

from app.users.auth import fastapi_users_backend, auth_backend
from app.users.models import User
from app.users.schemas import UserCreate, UserRead
from app.users.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth/jwt",
    tags=["auth"]
)


@app.get('/')
async def hello(user: str = 'User'):
    return {'message': f'Hello {user}'}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='localhost')
