from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()

# We include static files (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Connecting templates for HTML rendering
templates = Jinja2Templates(directory="public")

# Home page
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Catalog
@app.get("/catalog", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("catalog.html", {"request": request})

# Shopping cart
@app.get("/cart", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("shopping_cart.html", {"request": request})

# 404
@app.exception_handler(StarletteHTTPException)
async def custom_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse('404.html', {'request': request})
    else:
        return await http_exception_handler(request, exc)