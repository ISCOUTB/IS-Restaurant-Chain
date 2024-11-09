from domain.entities.inventory import Inventory, InventoryUpdate
from infrastructure.repositories.inventory_repository import InventoryRepository

class InventoryUseCases:
    def __init__(self, inventory_repo: InventoryRepository):
        self.inventory_repo = inventory_repo

    def add_inventory(self, inventory: Inventory) -> Inventory:
        if not inventory.product_id:
            raise ValueError("Product ID is required")
        if not inventory.name:
            raise ValueError("Name is required")
        if not inventory.stock or inventory.stock != 0:
            raise ValueError("Stock is required")
        if not inventory.price or inventory.price != 0:
            raise ValueError("Price is required")
        if self.inventory_repo.get_inventory(inventory.product_id):
            raise ValueError("Inventory already exists")
        return self.inventory_repo.create_inventory(inventory.product_id, inventory.name, 
                                                    inventory.stock, inventory.price, 
                                                    inventory.description)

    def get_inventory(self, product_id: int) -> Inventory:
        if not self.inventory_repo.get_inventory(product_id):
            raise ValueError("Inventory does not exist")
        return self.inventory_repo.get_inventory(product_id)

    def update_inventory(self, product_id: int, inventoryUpdate: InventoryUpdate) -> InventoryUpdate:
        if not self.inventory_repo.get_inventory(product_id):
            raise ValueError("Inventory does not exist")
        return self.inventory_repo.update_inventory(product_id, inventoryUpdate)

    def delete_inventory(self, product_id: int) -> bool:
        if not self.inventory_repo.get_inventory(product_id):
            raise ValueError("Inventory does not exist")
        return self.inventory_repo.delete_inventory(product_id)