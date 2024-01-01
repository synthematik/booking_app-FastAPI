from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.bookings.router import router as bookings_router
from src.users.router import router as users_router
from src.hotels.router import router as hotels_router
from src.hotels.rooms.router import router as rooms_router
from src.pages.router import router as pages_router
from src.files.router import router as files_router


app = FastAPI(debug=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users_router)

app.include_router(bookings_router)

app.include_router(hotels_router)

app.include_router(rooms_router)

app.include_router(pages_router)

app.include_router(files_router)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATH", "OPTIONS"],
    allow_headers=["*"],
)
