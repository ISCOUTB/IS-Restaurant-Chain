from pydantic import BaseModel
class Inventory(BaseModel):
    product_id: int
    name:str
    stock: int
    price: float
    description: str