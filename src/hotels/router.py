from datetime import date, datetime

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from src.exception import (CannotBookHotelForLongTime,
                           DateFromCannotBeAfterDateTo)
from src.hotels.schemas import SHotelInfo
from src.hotels.service import HotelService

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)


@router.get("/")
async def get_all_hotels() -> list[SHotelInfo]:
    hotels = await HotelService.find_all()
    return hotels


@router.get("/{location}/", name="get_hotel_by_location")
@cache(expire=1000)
async def get_hotels_by_location(
        location: str,
        date_from: date = Query(..., description=f"Например: {datetime.now().date()}"),
        date_to: date = Query(..., description=f"Например: {datetime.now().date()}"),
) -> list[SHotelInfo]:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongTime
    hotels = await HotelService.find_all_hotels(location, date_from, date_to)
    return hotels
