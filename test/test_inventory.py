import unittest
from unittest.mock import MagicMock
from domain.entities.inventory import Inventory
from interfaces.inventory_service import InventoryService
from domain.use_cases.inventory_use_cases import InventoryUseCases
from pydantic import ValidationError

class TestInventory(unittest.TestCase):
    
    def setUp(self):
            self.inventory_use_cases = MagicMock(spec=InventoryUseCases)
            self.inventory_service = InventoryService(self.inventory_use_cases)


    def test_create_inventory(self):
        inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
        self.assertEqual(inventory.product_id, 1)
        self.assertEqual(inventory.name, "Product A")
        self.assertEqual(inventory.stock, 100)
        self.assertEqual(inventory.price, 9.99)
        self.assertEqual(inventory.description, "Description of Product A")
        
    def test_add_inventory(self):
            inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
            self.inventory_use_cases.add_inventory.return_value = inventory

            result = self.inventory_service.add_inventory(inventory)

            self.inventory_use_cases.add_inventory.assert_called_once_with(inventory)
            self.assertEqual(result, inventory)

    def test_get_inventory(self):
            inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
            self.inventory_use_cases.get_inventory.return_value = inventory

            result = self.inventory_service.get_inventory(1)

            self.inventory_use_cases.get_inventory.assert_called_once_with(1)
            self.assertEqual(result, inventory)

    def test_update_inventory(self):
            inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
            self.inventory_use_cases.update_inventory.return_value = True

            result = self.inventory_service.update_inventory(1, inventory)

            self.inventory_use_cases.update_inventory.assert_called_once_with(1, inventory)
            self.assertTrue(result)

    def test_delete_inventory(self):
            self.inventory_use_cases.delete_inventory.return_value = True

            result = self.inventory_service.delete_inventory(1)

            self.inventory_use_cases.delete_inventory.assert_called_once_with(1)
            self.assertTrue(result)
            
    def test_delete_inventory_not_found(self):
            self.inventory_use_cases.delete_inventory.return_value = False

            with self.assertRaises(Exception):
                self.inventory_service.delete_inventory(9)

            self.inventory_use_cases.delete_inventory.assert_called_once_with(9)

    def test_create_inventory_invalid_price(self):
        inventory_1 = Inventory(product_id=1, name="Product A", stock=100, price="invalid-price", description="Description of Product A")
        with self.assertRaises(ValidationError):
            self.inventory_use_cases.add_inventory.return_value = inventory_1
            result = self.inventory_service.add_inventory(inventory_1)
            self.inventory_use_cases.add_inventory.assert_called_once_with(inventory_1)
            self.assertEqual(result, inventory_1)

            #Inventory(product_id=1, name="Product A", stock=100, price="invalid-price", description="Description of Product A")

    def test_create_inventory_negative_stock(self):
        with self.assertRaises(ValidationError):
            Inventory(product_id=1, name="Product A", stock=-10, price=9.99, description="Description of Product A")

    def test_create_inventory_missing_fields(self):
        with self.assertRaises(ValidationError):
            Inventory(product_id=1, name="Product A", price=9.99, description="Description of Product A")

    def test_create_inventory_empty_name(self):
        with self.assertRaises(ValidationError):
            Inventory(product_id=1, name="", stock=100, price=9.99, description="Description of Product A")

if __name__ == '__main__':
    unittest.main()
    
    
    
