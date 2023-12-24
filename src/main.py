from fastapi import FastAPI

from src.bookings.router import router as bookings_router
from src.users.router import router as users_router


app = FastAPI(debug=True)

app.include_router(bookings_router)

app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
