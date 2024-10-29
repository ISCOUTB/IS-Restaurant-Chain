from domain.entities.inventory import Inventory
from infrastructure.repositories.inventory_repository import InventoryRepository

class InventoryUseCases:
    def __init__(self, inventory_repo: InventoryRepository):
        self.inventory_repo = inventory_repo

    def add_inventory(self, inventory: Inventory) -> Inventory:
        return self.inventory_repo.create_inventory(inventory.product_id, inventory.name, 
                                                    inventory.stock, inventory.price, 
                                                    inventory.description)

    def get_inventory(self, product_id: int) -> Inventory:
        return self.inventory_repo.get_inventory(product_id)

    def update_inventory(self, product_id: int, inventory: Inventory) -> bool:
        return self.inventory_repo.update_inventory(product_id, inventory)

    def delete_inventory(self, product_id: int) -> bool:
        return self.inventory_repo.delete_inventory(product_id)