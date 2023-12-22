from sqlalchemy import select

from src.database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def find_all_bookings(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
