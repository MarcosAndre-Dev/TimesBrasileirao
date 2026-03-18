from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates("app/templates")
home = APIRouter(tags=["home"])

@home.get("/")
async def page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@home.get("/times")
async def timesPage(request: Request):
    return templates.TemplateResponse("times.html", {"request": request})