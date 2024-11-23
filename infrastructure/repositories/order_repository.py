from datetime import datetime
from domain.entities.order import Order
from bson import ObjectId

class OrderRepository:
    def __init__(self, db):
        self.collection = db["Pedidos"]
        self.user_collection = db["Usuario"]
        self.inventory_collection = db["Inventario"]

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

    def create_order(self, _id: ObjectId, products, username: str, payment, 
                    order_status: str, order_date: datetime, total_price: float) -> Order:
        user_data = self.user_collection.find_one({"username": username}, {"_id": 0, "user_id": 1, "username": 1, "email": 1, "password": 1})
        if not user_data:
            raise ValueError("User not found")

        product_data_list = []
        for product in products:
            product_data = self.inventory_collection.find_one(
                {"product_id": product.product_id}, 
                {"_id": 0, "product_id": 1, "name": 1, "price": 1, "stock": 1, "description": 1}
            )
            if not product_data:
                raise ValueError(f"Product with id {product.product_id} not found")
            product_data_list.append(product_data)

        order_data = {
            "_id": _id,
            "products": product_data_list,
            "client": user_data,
            "payment": payment,
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

    def add_product_to_order(self, order_id: ObjectId, product_id: int) -> bool:
        product_data = self.inventory_collection.find_one({"product_id": product_id})
        if not product_data:
            raise ValueError(f"Product with id {product_id} not found")

        result = self.collection.update_one(
            {"_id": order_id},
            {"$push": {"products": product_data}}
        )
        return result.modified_count > 0

    def remove_product_from_order(self, order_id: ObjectId, product_id: int) -> bool:
        result = self.collection.update_one(
            {"_id": order_id},
            {"$pull": {"products": {"product_id": product_id}}}
        )
        return result.modified_count > 0

    def cancel_order(self, order_id: ObjectId) -> bool:
        result = self.collection.update_one(
            {"_id": order_id},
            {"$set": {"order_status": "cancelled"}}
        )
        return result.modified_count > 0

    def pay_order(self, order_id: ObjectId) -> bool:
        result = self.collection.update_one(
            {"_id": order_id},
            {"$set": {"payment": "completed", "order_status": "paid"}}
        )
        return result.modified_count > 0