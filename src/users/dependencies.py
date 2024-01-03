from datetime import datetime

from fastapi import Depends, Request
from jose import jwt, JWTError

from src.config import settings
from src.users.service import UserService
from src.exception import *


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormat

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException

    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIdNotFoundException

    user = await UserService.find_by_id(int(user_id))
    if not user:
        raise UserNotFoundException

    return user
