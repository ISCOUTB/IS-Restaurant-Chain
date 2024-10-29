from domain.entities.inventory import Inventory

class InventoryRepository:
    def __init__(self, db):
        self.collection = db["Inventario"]

    def get_inventory(self, product_id: int) -> Inventory:
        inventory_data = self.collection.find_one({"product_id": product_id})
        if inventory_data:
            return Inventory(**inventory_data)
        return None

    def update_inventory(self, product_id: int, inventory: Inventory) -> bool:
        result = self.collection.update_one(
            {"product_id": product_id},
            {"$set": inventory.dict()}
        )
        return result.modified_count > 0

    def create_inventory(self, product_id:int, name:str, 
                                                    stock:int, price:float, 
                                                    description ) -> Inventory:
        inventory_data = {
            "product_id": product_id,
            "name": name,
            "stock": stock,
            "price": price,
            "description": description}
        self.collection.insert_one(inventory_data)
        return True

    def delete_inventory(self, product_id: int) -> bool:
        result = self.collection.delete_one({"product_id": product_id})
        return result.deleted_count > 0

    def last(self) -> Inventory:
        inventory_data = self.collection.find().sort("product_id", -1).limit(1).next()
        return Inventory(**inventory_data)