# main.py
from fastapi import FastAPI
import uvicorn
from infrastructure.api.routes import user_routes
from infrastructure.api.routes import inventory_routes
from infrastructure.api.routes import payment_routes

app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(inventory_routes.router, prefix="/inventory", tags=["inventory"])
app.include_router(payment_routes.router, prefix="/pagos", tags=["pagos"])


if __name__ == "__main__":
    uvicorn.run('main:app')