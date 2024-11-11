# main.py
from fastapi import FastAPI
import uvicorn
from infrastructure.api.routes import user_routes, inventory_routes, order_routes


app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(inventory_routes.router, prefix="/inventory", tags=["inventory"])
app.include_router(order_routes.router, prefix="/order", tags=["order"])

if __name__ == "__main__":
    uvicorn.run("main:app")
