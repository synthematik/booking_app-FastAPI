from fastapi import APIRouter, HTTPException

from src.users.schemas import SUserRegister
from src.users.service import UserService
from src.users.auth import get_password_hash


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500, detail="None")
    hashed_password = get_password_hash(user_data.password)
    await UserService.add_data(email=user_data.email, password=hashed_password)
