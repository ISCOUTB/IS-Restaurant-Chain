from pymongo import MongoClient
from bson import ObjectId
from domain.entities.payment import Pago


class PaymentRepository:
    def __init__(self, db):
        self.db = db
        self.collection = self.db["Pagos"]

    def create_payment(self, payment):
        if self.collection.find_one({"_id": ObjectId(payment["_id"])}):
            raise ValueError("Payment already exists")
        payment["_id"] = ObjectId()
        self.collection.insert_one(payment)

    def get_payments(self):
        return [Pago(**payment) for payment in self.collection.find()]

    def get_payment(self, id):
        payment = self.collection.find_one({"_id": ObjectId(id)})
        if payment is None:
            raise ValueError("Payment not found")
        return Pago(**payment)

    def update_payment(self, id, payment):
        if not self.collection.find_one({"_id": ObjectId(id)}):
            raise ValueError("Payment not found")
        self.collection.update_one({"_id": ObjectId(id)}, {"$set": payment})

    def delete_payment(self, id):
        if not self.collection.find_one({"_id": ObjectId(id)}):
            raise ValueError("Payment not found")
        self.collection.delete_one({"_id": ObjectId(id)})