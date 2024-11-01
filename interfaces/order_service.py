from domain.use_cases.order_use_cases import OrderUseCases
from domain.entities.order import Order
from bson import ObjectId

class OrderService:
    def __init__(self, order_use_cases: OrderUseCases):
        self.order_use_cases = order_use_cases

    def add_order(self, order: Order) -> Order:
        return self.order_use_cases.add_order(order)

    def get_order(self, order_id: ObjectId) -> Order:
        return self.order_use_cases.get_order(order_id)

    def update_order(self, order_id: ObjectId, order: Order) -> bool:
        return self.order_use_cases.update_order(order_id, order)

    def delete_order(self, order_id: ObjectId) -> bool:
        return self.order_use_cases.delete_order(order_id)