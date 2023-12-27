from fastapi import APIRouter, Depends
from fastapi import Request

from src.bookings.service import *
from src.bookings.schemas import SBooking
from src.users.models import User
from src.users.dependencies import get_current_user


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_booking(user: User = Depends(get_current_user)):
    return await BookingService.find_all_bookings(user_id=user.id)


