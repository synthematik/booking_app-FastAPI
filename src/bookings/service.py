from src.bookings.models import Bookings
from src.service.base import BaseService


class BookingService(BaseService):
    model = Bookings


