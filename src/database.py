from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import settings
from sqlalchemy import NullPool

if settings.MODE == "TEST":
    DATABASE_URL = settings.get_test_database_url()
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.get_database_url()
    DATABASE_PARAMS = {}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

