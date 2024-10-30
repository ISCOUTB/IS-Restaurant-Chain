from pydantic import BaseModel
from infrastructure.repositories.user_repository import UserRepository
class Order(BaseModel):
    user_id: UserRepository.get_usuario_by_id
    items: list
    total_price: float
    status: str
    
class MicroserviceOrder:
    def __init__(self, order_id, user_id, items, total_price, status):
        self.order_id = order_id
        self.user_id = user_id  # This should be an instance of the User class
        self.items = items  # List of items in the order
        self.total_price = total_price
        self.status = status  # e.g., 'pending', 'completed', 'canceled'

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_price -= item.price

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Order {self.order_id} for {self.user.name}: {self.status} - Total: ${self.total_price:.2f}"