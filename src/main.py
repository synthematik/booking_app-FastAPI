from datetime import date
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Query, Depends
from src.bookings.router import router as bookings_router


app = FastAPI(debug=True)

app.include_router(bookings_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hotel/{hotel_id}/")  # {} - параметры пути
async def get_hotel(hotel_id: int, date_from, date_to):  # параметры запроса
    return {"hotel_id": hotel_id, "date_from": date_from, "date_to": date_to}


class GetHotelsArg:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None, # Опциональные аргументы, то есть могут быть нулевыми
            stars: Optional[int] = Query(None, ge=1, le=5),  # Ограничение кол-ва звезд от 1 до 5
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    address: str
    name: str
    stars: int
    has_spa: bool


@app.get("/hotels/")
def get_hotels(search_arg: GetHotelsArg = Depends()):
    hotels = [
        {
            "address": "ул.Гагарина, 1",
            "name": "Super Hotel",
            "stars": 5,
        },

        {
            "address": "ул.Пушкина, 2",
            "name": "Five Hotel",
            "stars": 4,
        }
    ]
    return search_arg


class SBookind(BaseModel):  # Схема данных
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings/")
def add_booking(booking: SBookind):
    pass
