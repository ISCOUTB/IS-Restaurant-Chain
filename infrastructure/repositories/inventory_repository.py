from bson.objectid import ObjectId
from domain.entities.inventory import Inventory

class InventoryRepository:
    def __init__(self, db):
        self.collection = db["Inventario"]

    def get_inventory(self, product_id: int) -> Inventory:
        inventory_data = self.collection.find_one({"_id": ObjectId(product_id)})
        if inventory_data:
            return Inventory(**inventory_data)
        return None

    def update_inventory(self, product_id: int, inventory: Inventory) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": inventory.dict()}
        )
        return result.modified_count > 0

    def create_inventory(self, inventory: Inventory) -> Inventory:
        inventory_data = inventory.dict()
        inventory_data["_id"] = ObjectId(inventory_data["product_id"])
        self.collection.insert_one(inventory_data)
        return inventory

    def delete_inventory(self, product_id: int) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(product_id)})
        return result.deleted_count > 0

    def last(self) -> Inventory:
        inventory_data = self.collection.find().sort("_id", -1).limit(1).next()
        return Inventory(**inventory_data)