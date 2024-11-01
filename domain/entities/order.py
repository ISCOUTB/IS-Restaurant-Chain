from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from bson import ObjectId
from domain.entities.inventory import Inventory
from domain.entities.user import User
from domain.entities.payment import Pago

class Order(BaseModel):
    _id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    products: List[Inventory]
    client: User
    payment: Pago
    order_status: str
    order_date: datetime
    total_price: float

    def calculate_total_price(self):
        self.total_price = sum(product.price for product in self.products)

    def update_order_status(self):
        self.order_status = "paid" if self.payment.estado == "completed" else "pending"

    class Config:
        arbitrary_types_allowed = True