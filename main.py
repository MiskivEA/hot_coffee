import uvicorn
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from app.users.auth import auth_backend
from app.users.models import User
from app.users.schemas import UserCreate, UserRead
from app.users.user_manager import get_user_manager
from app.users.router import user_router
from app.users.auth import fastapi_users


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
app.include_router(user_router)


@app.get('/')
async def hello(user: str = 'User'):
    return {'message': f'Hello {user}'}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='localhost')
