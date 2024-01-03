from src.tasks.celerys import celery_app

from PIL import Image

from pathlib import Path

from pydantic import EmailStr

from src.tasks.email_templates import create_bookings_confirmation_template, create_account_confirmation_templates

from src.config import settings
import smtplib


@celery_app.task
def process_picture(picture_file_path: str):
    im_path = Path(picture_file_path)
    image = Image.open(im_path)
    resized_image_one = image.resize((1000, 500))
    resized_image_two = image.resize((200, 100))
    resized_image_one.save(f"static/images/resized_one_{im_path.name}")
    resized_image_two.save(f"static/images/resized_two_{im_path.name}")


@celery_app.task
def send_email_confirm_message(booking: dict, email_to: EmailStr):
    #email_to_test = "XXXX@gmail.com"
    message = create_bookings_confirmation_template(booking=booking, email_to=email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(message)


@celery_app.task
def send_account_confirmation_message(user: dict, email_to: EmailStr):
    #email_to_test = "XXXX@gmail.com"
    message = create_account_confirmation_templates(user=user, email_to=email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(message)
