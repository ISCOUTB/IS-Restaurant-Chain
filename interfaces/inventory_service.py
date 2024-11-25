from domain.use_cases.inventory_use_cases import InventoryUseCases
from domain.entities.inventory import Inventory, InventoryUpdate


class InventoryService:
    def __init__(self, inventory_use_cases: InventoryUseCases):
        self.inventory_use_cases = inventory_use_cases

    def add_inventory(self, inventory: Inventory) -> Inventory:
        if not inventory.product_id:
            raise ValueError("Product ID is required")
        if not inventory.name:
            raise ValueError("Name is required")
        if not inventory.stock:
            raise ValueError("Stock is required")
        if not inventory.price:
            raise ValueError("Price is required")
        return self.inventory_use_cases.add_inventory(inventory)
    
    def get_all_inventory(self) -> list[Inventory]:
        return self.inventory_use_cases.get_all_inventory()
    
    def get_inventory(self, product_id: int) -> Inventory:
        if not product_id:
            raise ValueError("Product ID is required")
        return self.inventory_use_cases.get_inventory(product_id)

    def update_inventory(self, product_id: int, inventory_update: InventoryUpdate) -> InventoryUpdate:
        if not inventory_update.name:
            raise ValueError("Name is required")
        if not inventory_update.stock:
            raise ValueError("Stock is required")
        if not inventory_update.price:
            raise ValueError("Price is required")
        return self.inventory_use_cases.update_inventory(product_id, inventory_update)

    def delete_inventory(self, product_id: int) -> bool:
        if not product_id:
            raise ValueError("Product ID is required")
        return self.inventory_use_cases.delete_inventory(product_id)