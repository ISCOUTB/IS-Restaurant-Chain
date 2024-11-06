import unittest
from domain.entities.inventory import Inventory
from interfaces.inventory_service import InventoryService
from domain.use_cases.inventory_use_cases import InventoryUseCases
from infrastructure.repositories.dbcontroller import DbController
from pydantic import ValidationError

class TestInventoryIntegration(unittest.TestCase):
    def setUp(self):
        self.db_controller = DbController()
        self.inventory_use_cases = InventoryUseCases(self.db_controller.inventory_repo)
        self.inventory_service = InventoryService(self.inventory_use_cases)

    def test_add_and_get_inventory(self):
        inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
        self.inventory_service.add_inventory(inventory)

        result = self.inventory_service.get_inventory(1)
        
        self.assertEqual(result.product_id, 1)
        self.assertEqual(result.name, "Product A")
        self.assertEqual(result.stock, 100)
        self.assertEqual(result.price, 9.99)
        self.assertEqual(result.description, "Description of Product A")

    def test_update_inventory(self):
        inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
        self.inventory_service.add_inventory(inventory)

        updated_inventory = Inventory(product_id=1, name="Product A Updated", stock=150, price=19.99, description="Updated Description")
        self.inventory_service.update_inventory(1, updated_inventory)

        result = self.inventory_service.get_inventory(1)
        
        self.assertEqual(result.product_id, 1)
        self.assertEqual(result.name, "Product A Updated")
        self.assertEqual(result.stock, 150)
        self.assertEqual(result.price, 19.99)
        self.assertEqual(result.description, "Updated Description")

    def test_delete_inventory(self):
        inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
        self.inventory_service.add_inventory(inventory)

        self.inventory_service.delete_inventory(1)
        
        with self.assertRaises(Exception):  # Assuming an exception is raised when inventory is not found
            self.inventory_service.get_inventory(1)

    def test_add_inventory_with_negative_stock(self):
        with self.assertRaises(ValidationError):
            inventory = Inventory(product_id=1, name="Product A", stock=-10, price=9.99, description="Description of Product A")
            self.inventory_service.add_inventory(inventory)

    def test_add_inventory_with_empty_name(self):
        with self.assertRaises(ValidationError):
            inventory = Inventory(product_id=1, name="", stock=100, price=9.99, description="Description of Product A")
            self.inventory_service.add_inventory(inventory)

if __name__ == '__main__':
    unittest.main()