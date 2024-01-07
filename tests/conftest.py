import asyncio
from datetime import datetime

import pytest
import json

from sqlalchemy import insert

from src.config import settings
from src.database import Base, engine, async_session_maker

from src.users.models import User
from src.hotels.models import Hotel
from src.hotels.rooms.models import Room
from src.bookings.models import Bookings
from src.main import app as fastapi_app

from fastapi.testclient import TestClient
from httpx import AsyncClient


@pytest.fixture(autouse=True, scope="session")  # фикстура - функция, которая подготавливает определенную среду для тестирования
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    def open_json(model_name: str):
        with open(f"tests/mock_{model_name}.json", encoding="utf-8") as file:
            return json.load(file)

    hotels = open_json("hotels")
    rooms = open_json("rooms")
    users = open_json("users")
    bookings = open_json("bookings")

    for booking in bookings:
        booking["date_from"] = datetime.strptime(booking["date_from"], "%Y-%m-%d")
        booking["date_to"] = datetime.strptime(booking["date_to"], "%Y-%m-%d")

    async with async_session_maker() as session:
        add_hotels = insert(Hotel).values(hotels)
        add_rooms = insert(Room).values(rooms)
        add_users = insert(User).values(users)
        add_bookings = insert(Bookings).values(bookings)

        await session.execute(add_hotels)
        await session.execute(add_rooms)
        await session.execute(add_users)
        await session.execute(add_bookings)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function", autouse=True)
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def session():
    async with async_session_maker as session:
        yield session
