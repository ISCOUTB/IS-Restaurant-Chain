from bson import ObjectId
from domain.entities.order import Order
from infrastructure.repositories.order_repository import OrderRepository

class OrderUseCases:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    def add_order(self, order: Order) -> Order:
        return self.order_repo.create_order(order._id, order.products, order.client, 
                                            order.payment, order.order_status, 
                                            order.order_date, order.total_price)

    def get_order(self, order_id: ObjectId) -> Order:
        return self.order_repo.get_order(order_id)

    def update_order(self, order_id: ObjectId, order: Order) -> bool:
        return self.order_repo.update_order(order_id, order)

    def delete_order(self, order_id: ObjectId) -> bool:
        return self.order_repo.delete_order(order_id)