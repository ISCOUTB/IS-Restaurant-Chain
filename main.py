# main.py
from fastapi import FastAPI
import uvicorn
from infrastructure.api.routes import user_routes

app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run('main:app')