from fastapi import APIRouter, UploadFile
import shutil

from src.tasks.tasks import process_picture


router = APIRouter(
    prefix="/files",
    tags=["Загрузка файлов"]
)


@router.post("/hotels_images/")
async def add_hotels_images(name: int, file: UploadFile):
    path = f"static/images/{name}.webp"
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_picture.delay(path)
    return {"status": "success"}
