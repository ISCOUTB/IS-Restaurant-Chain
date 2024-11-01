from datetime import datetime
from domain.entities.order import Order
from bson import ObjectId

class OrderRepository:
    def __init__(self, db):
        self.collection = db["Pedidos"]

    def get_order(self, order_id: ObjectId) -> Order:
        order_data = self.collection.find_one({"_id": order_id})
        if order_data:
            return Order(**order_data)
        return None

    def update_order(self, order_id: ObjectId, order: Order) -> bool:
        result = self.collection.update_one(
            {"_id": order_id},
            {"$set": order.dict(by_alias=True)}
        )
        return result.modified_count > 0

    def create_order(self, _id: ObjectId, products, client, payment, 
                     order_status: str, order_date: datetime, total_price: float) -> Order:
        order_data = {
            "_id": _id,
            "products": [product.dict() for product in products],
            "client": client.dict(),
            "payment": payment.dict(),
            "order_status": order_status,
            "order_date": order_date,
            "total_price": total_price
        }
        self.collection.insert_one(order_data)
        return Order(**order_data)

    def delete_order(self, order_id: ObjectId) -> bool:
        result = self.collection.delete_one({"_id": order_id})
        return result.deleted_count > 0

    def last(self) -> Order:
        order_data = self.collection.find().sort("_id", -1).limit(1).next()
        return Order(**order_data)