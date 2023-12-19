from datetime import date
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hotel/{hotel_id}/")  # {} - параметры пути
async def get_hotel(hotel_id: int, date_from, date_to):  # параметры запроса
    return {"hotel_id": hotel_id, "date_from": date_from, "date_to": date_to}


@app.get("/hotels/")  # {} - параметры пути
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,  # Опциональные аргументы, то есть могут быть нулевыми
        stars: Optional[int] = Query(None, ge=1, le=5),  # Ограничение кол-ва звезд от 1 до 5
):
    return {"location": location, "date_from": date_from, "date_to": date_to, "stars": stars, "has_spa": has_spa}
