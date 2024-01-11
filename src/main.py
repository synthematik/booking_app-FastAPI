import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.requests import Request
from redis import asyncio as aioredis
from sqladmin import Admin

from src.admin.admin import *
from src.admin.auth import authentication_backend
from src.bookings.router import router as bookings_router
from src.config import settings
from src.database import engine
from src.files.router import router as files_router
from src.hotels.rooms.router import router as rooms_router
from src.hotels.router import router as hotels_router
from src.pages.router import router as pages_router
from src.users.router import router as users_router
from src.logger import logger

app = FastAPI(debug=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users_router)

app.include_router(bookings_router)

app.include_router(hotels_router)

app.include_router(rooms_router)

app.include_router(pages_router)

app.include_router(files_router)

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATH", "OPTIONS"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        decode_responses=True,
        encoding="utf-8",
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)

admin.add_view(HotelAdmin)

admin.add_view(BookingsAdmin)

admin.add_view(RoomAdmin)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info("Request processing time: ", extra={
        "method": request.method,
        "process_time": round(process_time, 4)
    })
    return response
