from src.tasks.celerys import celery_app

from PIL import Image

from pathlib import Path


@celery_app.task
def process_picture(picture_file_path: str):
    im_path = Path(picture_file_path)
    image = Image.open(im_path)
    resized_image_one = image.resize((1000, 500))
    resized_image_two = image.resize((200, 100))
    resized_image_one.save(f"static/images/resized_one_{im_path.name}")
    resized_image_two.save(f"static/images/resized_two_{im_path.name}")
