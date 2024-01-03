from email.message import EmailMessage

from pydantic import EmailStr

from src.config import settings


def create_bookings_confirmation_template(
        booking: dict,
        email_to: EmailStr,
):
    email_message = EmailMessage()
    email_message["Subject"] = "Подтверждение бронирования"
    email_message["From"] = settings.SMTP_USER
    email_message["To"] = email_to

    email_message.set_content(
        f"""
            <h2>Подтвердите бронирование</h2>
            <h3>Вы забронировали отель с {booking["date_from"]} по {booking["date_to"]}</h3>
        """,
        subtype="html"
    )

    return email_message


def create_account_confirmation_templates(
        user: dict,
        email_to: EmailStr
):
    email_message = EmailMessage()
    email_message["Subject"] = "Подтверждение регистрации"
    email_message["From"] = settings.SMTP_USER
    email_message["To"] = email_to

    email_message.set_content(
        f"""
            <h1>Подтвердите регистрацию</h1>
            <p>Вы зарегистрировались на моем сайте с почтой {user["email"]}</p>
        """,
        subtype="html"
    )

    return email_message


