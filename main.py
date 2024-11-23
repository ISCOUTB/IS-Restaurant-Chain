# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from infrastructure.api.routes import user_routes, inventory_routes



app = FastAPI()
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
user = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def template_register(request: Request):
    return user.TemplateResponse("Home.html", {"request": request})

app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(inventory_routes.router, prefix="/inventory", tags=["inventory"])

if __name__ == "__main__":
    uvicorn.run("main:app")
