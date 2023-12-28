from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    default_detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.default_detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Пользователь с такой почтой уже существует"


class UserIncorrectPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Неверный email или пароль"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Токен истек"


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Токен отсутствует"


class IncorrectTokenFormat(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Некорректный формат токена"


class UserIdNotFoundException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserNotFoundException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED

