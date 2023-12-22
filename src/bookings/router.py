from fastapi import APIRouter

from src.bookings.service import *
from src.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_booking() -> list[SBooking]:
    result = await BookingService.find_all_bookings()
    return result

