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
        if not inventory.stock or inventory.stock != 0:
            raise ValueError("Stock is required")
        if not inventory.price or inventory.price != 0:
            raise ValueError("Price is required")
        return self.inventory_use_cases.add_inventory(inventory)

    def get_inventory(self, product_id: int) -> Inventory:
        if not product_id:
            raise ValueError("Product ID is required")
        return self.inventory_use_cases.get_inventory(product_id)

    def update_inventory(self, product_id: int, inventoryUpdate: InventoryUpdate) -> InventoryUpdate:
        if not inventoryUpdate.name:
            raise ValueError("Name is required")
        if not inventoryUpdate.stock:
            raise ValueError("Stock is required")
        if not inventoryUpdate.price:
            raise ValueError("Price is required")
        return self.inventory_use_cases.update_inventory(product_id, inventoryUpdate)

    def delete_inventory(self, product_id: int) -> bool:
        if not product_id:
            raise ValueError("Product ID is required")
        return self.inventory_use_cases.delete_inventory(product_id)