from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.users.service import UserService
from src.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate(email: EmailStr, password: str):
    existing_user = await UserService.find_one_or_none(email=email)
    if not existing_user or not verify_password(password, existing_user.password):
        return None
    return existing_user


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.KEY, settings.ALGORITHM
    )
    return encode_jwt

