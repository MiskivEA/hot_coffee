from fastapi_users import FastAPIUsers
from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend

from app.env_configs import get_jwt_secret
from app.users.models import User
from app.users.user_manager import get_user_manager

# transport
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# strategy
SECRET = get_jwt_secret()


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=36000)


# backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# fast api users
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
