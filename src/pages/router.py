from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.hotels.router import get_all_hotels, get_hotels_by_location

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)

templates = Jinja2Templates(directory="templates/")


@router.get("/", name='root')
async def root(request: Request):
    return templates.TemplateResponse("base_app.html", {"request": request})


@router.get("/login/", name='login', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("auth/login_user.html", {"request": request})


@router.get("/register/")
async def register(request: Request):
    return templates.TemplateResponse("auth/register_user.html", {"request": request})


@router.get("/hotels/", name='hotels_list')
async def get_hotels_page(
        request: Request,
        hotels=Depends(get_all_hotels)
):
    return templates.TemplateResponse(
        "hotels/hotels.html",
        {
            "request": request,
            "hotels": hotels,
        }
    )


@router.get("/{location}/")
async def get_hotels_by_location_page(
        request: Request,
        hotels=Depends(get_hotels_by_location)
):
    return templates.TemplateResponse(
        "hotels/hotels_location.html", {
            "request": request,
            "hotels": hotels,
        }
    )
