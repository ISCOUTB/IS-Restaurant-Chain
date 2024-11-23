import unittest
from bson import ObjectId
from datetime import datetime
from domain.entities.order import Order
from domain.entities.inventory import Inventory
from domain.entities.user import User
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.order_use_cases import OrderUseCases
from interfaces.order_service import OrderService
from pydantic import ValidationError

class TestOrderIntegration(unittest.TestCase):
    def setUp(self):
        self.db_controller = DbController()
        self.order_use_cases = OrderUseCases(self.db_controller.order_repo)
        self.order_service = OrderService(self.order_use_cases)

    def test_create_and_get_order(self):
        order_id = ObjectId()
        products = [Inventory(product_id=1, name="Product A", price=9.99, stock=100, description="Description of Product A")]
        client = User(user_id=666, username="testing2", email="testing2@example.com", password="password")
        payment = "pending"
        order = Order(id=order_id, products=products, client=client, payment=payment, 
                      order_status="new", order_date=datetime.now(), total_price=9.99)
        
        self.order_service.add_order(order)

        result = self.order_service.get_order(order_id)

        self.assertEqual(result.id, order_id)
        self.assertEqual(result.products[0].product_id, 1)
        self.assertEqual(result.products[0].name, "Product A")
        self.assertEqual(result.products[0].price, 9.99)
        self.assertEqual(result.client.username, "testing2")
        self.assertEqual(result.client.email, "testing2@example.com")
        self.assertEqual(result.payment, "pending")
        self.assertEqual(result.order_status, "new")
        self.assertEqual(result.total_price, 9.99)

    def test_update_order(self):
        order_id = ObjectId()
        products = [Inventory(product_id=1, name="Product A", price=9.99, stock=100, description="Description of Product A")]
        client = User(user_id=666, username="testing2", email="testing2@example.com", password="password")
        payment = "pending"
        order = Order(id=order_id, products=products, client=client, payment=payment, 
                      order_status="new", order_date=datetime.now(), total_price=9.99)
        
        self.order_service.add_order(order)

        updated_order = Order(id=order_id, products=products, client=client, payment="completed", 
                              order_status="paid", order_date=datetime.now(), total_price=9.99)
        self.order_service.update_order(order_id, updated_order)

        result = self.order_service.get_order(order_id)

        self.assertEqual(result.payment, "completed")
        self.assertEqual(result.order_status, "paid")

    def test_delete_order(self):
        order_id = ObjectId()
        products = [Inventory(product_id=1, name="Product A", price=9.99, stock=100, description="Description of Product A")]
        client = User(user_id=666, username="testing2", email="testing2@example.com", password="password")
        payment = "pending"
        order = Order(id=order_id, products=products, client=client, payment=payment, 
                      order_status="new", order_date=datetime.now(), total_price=9.99)
        
        self.order_service.add_order(order)

        self.order_service.delete_order(order_id)

        result = self.order_service.get_order(order_id)

        self.assertIsNone(result)

    def test_add_order_with_invalid_total_price(self):
        order_id = ObjectId()
        products = [Inventory(product_id=1, name="Product A", price=9.99, stock=100, description="Description of Product A")]
        client = User(user_id=666, username="testing2", email="testing2@example.com", password="password")
        payment = "pending"
        with self.assertRaises(ValidationError):
            Order(id=order_id, products=products, client=client, payment=payment, 
                  order_status="new", order_date=datetime.now(), total_price="invalid-price")

    def test_add_order_with_missing_fields(self):
        order_id = ObjectId()
        products = [Inventory(product_id=1, name="Product A", price=9.99, stock=100, description="Description of Product A")]
        client = User(user_id=666, username="testing2", email="testing2@example.com", password="password")
        payment = "pending"
        with self.assertRaises(ValidationError):
            Order(id=order_id, products=products, client=client, payment=payment, 
                  order_status="new", order_date=datetime.now())

    def test_add_order_with_empty_client_name(self):
        order_id = ObjectId()
        products = [Inventory(product_id=1, name="Product A", price=9.99, stock=100, description="Description of Product A")]
        client = User(user_id=666, username="", email="testing2@example.com", password="password")
        payment = "pending"
        with self.assertRaises(ValidationError):
            Order(id=order_id, products=products, client=client, payment=payment, 
                  order_status="new", order_date=datetime.now(), total_price=9.99)

if __name__ == '__main__':
    unittest.main()