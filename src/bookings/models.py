from src.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Computed


class Bookings(Base):
    __tablename__ = "bookings"

    id = Column("id", Integer, primary_key=True, index=True)
    room_id = Column("room_id", ForeignKey("rooms.id"))
    user_id = Column("user_id", ForeignKey("users.id"))
    date_from = Column("date_from", Date, nullable=False)
    date_to = Column("date_to", Date, nullable=False)
    price = Column("price", Integer, nullable=False)
    total_cost = Column("total_cost", Integer, Computed("(date_to - date_from) * price"))
    total_days = Column("total_days", Integer, Computed("(date_to-date_from)"))
