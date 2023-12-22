from fastapi import APIRouter
from src.database import async_session_maker
from src.bookings.models import Bookings
from sqlalchemy import select
from src.bookings.service import *


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_booking():
    result = await BookingService.find_all_bookings()
    return result

