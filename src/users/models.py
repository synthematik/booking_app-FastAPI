from src.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, index=True)
    email = Column("email", String, nullable=False)
    hashed_password = Column("password", String)
