from domain.use_cases.inventory_use_cases import InventoryUseCases
from domain.entities.inventory import Inventory

class InventoryService:
    def __init__(self, inventory_use_cases: InventoryUseCases):
        self.inventory_use_cases = inventory_use_cases

    def add_inventory(self, inventory: Inventory) -> Inventory:
        return self.inventory_use_cases.add_inventory(inventory)

    def get_inventory(self, product_id: int) -> Inventory:
        return self.inventory_use_cases.get_inventory(product_id)

    def update_inventory(self, product_id: int, inventory: Inventory) -> bool:
        return self.inventory_use_cases.update_inventory(product_id, inventory)

    def delete_inventory(self, product_id: int) -> bool:
        return self.inventory_use_cases.delete_inventory(product_id)