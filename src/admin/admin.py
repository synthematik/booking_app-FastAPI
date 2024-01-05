from src.hotels.models import Hotel
from src.users.models import User
from src.bookings.models import Bookings
from src.hotels.rooms.models import Room

from sqladmin import ModelView


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.booking]
    name_plural = "Пользователи"
    name = "Пользователь"
    icon = "fa-solid fa-user"
    column_details_exclude_list = [User.hashed_password]


class HotelAdmin(ModelView, model=Hotel):
    column_list = [c.name for c in Hotel.__table__.c] + [Hotel.room]
    name_plural = "Отели"
    name = "Отель"
    icon = "fa-solid fa-hotel"


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user]
    name_plural = "Бронирования"
    name = "Бронь"
    icon = "fa-solid fa-book"


class RoomAdmin(ModelView, model=Room):
    column_list = [c.name for c in Room.__table__.c] + [Room.booking, Room.hotel]
    name_plural = "Комнаты"
    name = "Комната"
    icon = "fa-solid fa-bed"

