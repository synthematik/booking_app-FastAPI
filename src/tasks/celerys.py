from celery import Celery

from src.config import settings


celery_app = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=["src.tasks.tasks"],
    broker_connection_retry_on_startup=True,
)


