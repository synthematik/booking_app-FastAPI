from fastapi import APIRouter, Depends
from pydantic import parse_obj_as

from src.bookings.schemas import SBooking
from src.bookings.service import *
from src.exception import *
from src.tasks.tasks import send_email_confirm_message
from src.users.dependencies import get_current_user
from src.users.models import User

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_booking(user: User = Depends(get_current_user)) -> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)


@router.post("")
async def create_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: User = Depends(get_current_user),
):
    booking = await BookingService.create(user.id, room_id, date_from, date_to)
    bookings_dict = parse_obj_as(SBooking, booking).dict()
    if not booking:
        raise RoomCantBeBookedException()
    send_email_confirm_message.delay(bookings_dict, user.email)
    return bookings_dict


@router.delete("/{booking_id}/")
async def delete_booking(booking_id: int, user: User = Depends(get_current_user)):
    await BookingService.delete(id=booking_id, user_id=user.id)
    return {"status": 200}
