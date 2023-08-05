from fastapi_users.authentication import BearerTransport
from app.env_configs import get_jwt_secret

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
