from fastapi import FastAPI

from src.bookings.router import router as bookings_router
from src.users.router import router as users_router
from src.hotels.router import router as hotels_router
from src.hotels.rooms.router import router as rooms_router


app = FastAPI(debug=True)

app.include_router(users_router)

app.include_router(bookings_router)

app.include_router(hotels_router)

app.include_router(rooms_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
