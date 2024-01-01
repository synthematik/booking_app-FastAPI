from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.hotels.router import get_hotels_by_location, get_all_hotels


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)


templates = Jinja2Templates(directory="templates/")


@router.get("/", name='root')
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/hotels/", name='hotels_list')
async def get_hotels_page(request: Request, hotels=Depends(get_all_hotels)):
    return templates.TemplateResponse("hotels.html", {"request": request, "hotels": hotels})

