from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend

from app.env_configs import get_jwt_secret

# transport
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# strategy
SECRET = get_jwt_secret()


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


# backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
