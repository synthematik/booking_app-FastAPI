from sqlalchemy import select, insert

from src.database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        """
        Функция возвращает либо конкретные данные по id, либо пустоту
        """
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """
        Функция возвращает либо конкретные данные по фильтру, либо пустоту
        """
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_data(cls, **data):
        """
        Функция для добавления данных в базу
        """
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()

