from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class Inventory(BaseModel):
    product_id: int
    name: str
    stock: int
    price: float
    description: Optional[str] = None

class User(BaseModel):
    user_id: float
    username: str
    email: EmailStr
    password: str

class Order(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    products: List[Inventory]
    client: User
    payment: str
    order_status: str
    order_date: datetime
    total_price: float

    def calculate_total_price(self):
        self.total_price = sum(product.price for product in self.products)

    def update_order_status(self):
        self.order_status = "paid" if self.payment == "completed" else "pending"

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True