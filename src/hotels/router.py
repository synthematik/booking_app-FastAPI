from datetime import date

from fastapi import APIRouter

from src.hotels.service import HotelService
from src.hotels.schemas import SHotelInfo
from src.exception import DateFromCannotBeAfterDateTo, CannotBookHotelForLongTime


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)


@router.get("/")
async def get_all_hotels() -> list[SHotelInfo]:
    hotels = await HotelService.find_all()
    return hotels


@router.get("/{location}/", name="get_hotel_by_location")
async def get_hotels_by_location(
        location: str, date_from: date, date_to: date
) -> list[SHotelInfo]:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongTime
    hotels = await HotelService.find_all_hotels(location, date_from, date_to)
    return hotels




