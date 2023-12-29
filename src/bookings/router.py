from fastapi import APIRouter, Depends

from src.bookings.service import *
from src.bookings.schemas import SBooking
from src.users.models import User
from src.users.dependencies import get_current_user
from src.exception import *


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_booking(user: User = Depends(get_current_user)) -> list[SBooking]:
    return await BookingService.find_all_bookings(user_id=user.id)


@router.post("")
async def create_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: User = Depends(get_current_user),
):
    booking = await BookingService.create(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCantBeBookedException()
