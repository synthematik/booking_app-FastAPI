from fastapi import APIRouter, UploadFile
import shutil


router = APIRouter(
    prefix="/files",
    tags=["Загрузка файлов"]
)


@router.post("/hotels_images/")
async def add_hotels_images(name: int, file: UploadFile):
    with open(f"static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return {"status": "success"}
