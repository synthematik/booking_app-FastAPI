from datetime import date

from sqlalchemy import and_, func, insert, or_, select

from src.bookings.models import Bookings
from src.database import async_session_maker
from src.hotels.rooms.models import Room
from src.service.base import BaseService


class BookingService(BaseService):
    model = Bookings

    @classmethod
    async def create(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        """
        Реализация такого sql запрос:
        with booked_rooms as (select *
            from bookings
            where room_id = 1 and
            (date_from >= '2033-05-15' and date_from <= '2033-06-20') or
            (date_from <= '2033-05-15' and date_to > '2033-05-15')
        )
        select r.quantity - count(b.room_id)
        from rooms r
        left join booked_rooms b on (b.room_id=r.id)
        where r.id = 1
        group by r.quantity, b.room_id
        """
        async with async_session_maker() as session:
            booked_rooms = (
                select(Bookings)
                .where(
                    and_(
                        Bookings.room_id == room_id,
                        or_(
                            and_(
                                Bookings.date_from >= date_from,
                                Bookings.date_from <= date_to,
                            ),
                            and_(
                                Bookings.date_from <= date_from,
                                Bookings.date_to > date_from,
                            ),
                        ),
                    )
                )
                .cte("booked_rooms")
            )

            get_rooms_left = (
                select(
                    (Room.quantity - func.count(booked_rooms.c.room_id)).label(
                        "rooms_left"
                    )
                )
                .select_from(Room)
                .join(booked_rooms, booked_rooms.c.room_id == Room.id, isouter=True)
                .where(Room.id == room_id)
                .group_by(Room.quantity, booked_rooms.c.room_id)
            )

            rooms_left = await session.execute(get_rooms_left)
            roooms_left: int = rooms_left.scalar()

            if roooms_left > 0:
                get_price = select(Room.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = (
                    insert(Bookings)
                    .values(
                        room_id=room_id,
                        user_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    )
                    .returning(Bookings)
                )

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            else:
                return None
