from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", String, nullable=False)
    location = Column("location", String, nullable=False)
    services = Column("services", JSON)
    rooms_quantity = Column("rooms_quantity", Integer, nullable=False)
    image_id = Column("image_id", Integer)
    stars = Column("stars", Integer, nullable=False)

    room = relationship("Room", back_populates="hotel")

    def __str__(self):
        return f"Hotel name - {self.name}"
