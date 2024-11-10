from pydantic import BaseModel
from typing import Optional

class Inventory(BaseModel):
    product_id: int
    name: str
    stock: int
    price: float
    description: Optional[str] = None

class InventoryUpdate(BaseModel):
    name: Optional[str]
    stock: Optional[int]
    price: Optional[float]
    description: Optional[str]