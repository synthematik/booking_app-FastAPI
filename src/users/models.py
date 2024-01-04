from src.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, index=True)
    email = Column("email", String, nullable=False)
    hashed_password = Column("password", String)

    booking = relationship("Bookings", back_populates="user")

    def __str__(self):
        return f"User - {self.email}"
