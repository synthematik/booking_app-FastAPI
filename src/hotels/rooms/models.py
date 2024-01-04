from sqlalchemy.orm import relationship

from src.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey


class Room(Base):
    __tablename__ = "rooms"

    id = Column("id", Integer, primary_key=True)
    hotel_id = Column("hotel_id", ForeignKey("hotels.id"))
    name = Column("name", String)
    description = Column("description", String)
    price = Column("price", Integer)
    services = Column("services", JSON)
    quantity = Column("quantity", Integer)
    image_id = Column("image_id", Integer)

    booking = relationship("Bookings", back_populates="room")
    hotel = relationship("Hotel", back_populates="room")

    def __str__(self):
        return f"Room - {self.name}"
