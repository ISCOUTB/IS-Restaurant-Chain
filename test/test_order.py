import unittest
from unittest.mock import MagicMock
from domain.entities.order import Order
from domain.entities.inventory import Inventory
from domain.entities.user import User
from domain.entities.payment import Pago
from interfaces.order_service import OrderService
from domain.use_cases.order_use_cases import OrderUseCases
from pydantic import ValidationError
from bson import ObjectId
from datetime import datetime

class TestOrder(unittest.TestCase):
    
    def setUp(self):
        self.order_use_cases = MagicMock(spec=OrderUseCases)
        self.order_service = OrderService(self.order_use_cases)

    def test_create_order(self):
        order_id = ObjectId()
        products = [Inventory(product_id=ObjectId(), name="Product A", price=9.99)]
        client = User(user_id=ObjectId(), name="John Doe", email="john.doe@example.com")
        payment = Pago(payment_id=ObjectId(), method="Efectivo", estado="pendiente")
        order = Order(_id=order_id, products=products, client=client, payment=payment, 
                      order_status="pending", order_date=datetime.now(), total_price=9.99)
        
        self.assertEqual(order._id, order_id)
        self.assertEqual(order.products, products)
        self.assertEqual(order.client, client)
        self.assertEqual(order.payment, payment)
        self.assertEqual(order.order_status, "pending")
        self.assertEqual(order.total_price, 9.99)

    def test_add_order(self):
        order_id = ObjectId()
        products = [Inventory(product_id=ObjectId(), name="Product A", price=9.99)]
        client = User(user_id=ObjectId(), name="John Doe", email="john.doe@example.com")
        payment = Pago(payment_id=ObjectId(), method="Efectivo", estado="pendiente")
        order = Order(_id=order_id, products=products, client=client, payment=payment, 
                      order_status="pending", order_date=datetime.now(), total_price=9.99)
        
        self.order_use_cases.add_order.return_value = order

        result = self.order_service.add_order(order)

        self.order_use_cases.add_order.assert_called_once_with(order)
        self.assertEqual(result, order)

    def test_get_order(self):
        order_id = ObjectId()
        products = [Inventory(product_id=ObjectId(), name="Product A", price=9.99)]
        client = User(user_id=ObjectId(), name="John Doe", email="john.doe@example.com")
        payment = Pago(payment_id=ObjectId(), method="Efectivo", estado="pendiente")
        order = Order(_id=order_id, products=products, client=client, payment=payment, 
                      order_status="pending", order_date=datetime.now(), total_price=9.99)
        
        self.order_use_cases.get_order.return_value = order

        result = self.order_service.get_order(order_id)

        self.order_use_cases.get_order.assert_called_once_with(order_id)
        self.assertEqual(result, order)

    def test_update_order(self):
        order_id = ObjectId()
        products = [Inventory(product_id=ObjectId(), name="Product A", price=9.99)]
        client = User(user_id=ObjectId(), name="John Doe", email="john.doe@example.com")
        payment = Pago(payment_id=ObjectId(), method="Efectivo", estado="pendiente")
        order = Order(_id=order_id, products=products, client=client, payment=payment, 
                      order_status="pending", order_date=datetime.now(), total_price=9.99)
        
        self.order_use_cases.update_order.return_value = True

        result = self.order_service.update_order(order_id, order)

        self.order_use_cases.update_order.assert_called_once_with(order_id, order)
        self.assertTrue(result)

    def test_delete_order(self):
        order_id = ObjectId()
        self.order_use_cases.delete_order.return_value = True

        result = self.order_service.delete_order(order_id)

        self.order_use_cases.delete_order.assert_called_once_with(order_id)
        self.assertTrue(result)
        
    def test_delete_order_not_found(self):
        order_id = ObjectId()
        self.order_use_cases.delete_order.return_value = False

        with self.assertRaises(Exception):
            self.order_service.delete_order(order_id)

        self.order_use_cases.delete_order.assert_called_once_with(order_id)

    def test_create_order_invalid_total_price(self):
        order_id = ObjectId()
        products = [Inventory(product_id=ObjectId(), name="Product A", price="invalid-price")]
        client = User(user_id=ObjectId(), name="John Doe", email="john.doe@example.com")
        payment = Pago(payment_id=ObjectId(), method="Efectivo", estado="pendiente")
        with self.assertRaises(ValidationError):
            Order(_id=order_id, products=products, client=client, payment=payment, 
                  order_status="pending", order_date=datetime.now(), total_price="invalid-price")

    def test_create_order_missing_fields(self):
        order_id = ObjectId()
        products = [Inventory(product_id=ObjectId(), name="Product A", price=9.99)]
        client = User(user_id=ObjectId(), name="John Doe", email="john.doe@example.com")
        payment = Pago(payment_id=ObjectId(), method="Efectivo", estado="pendiente")
        with self.assertRaises(ValidationError):
            Order(_id=order_id, products=products, client=client, payment=payment, 
                  order_status="pending", order_date=datetime.now())

    def test_create_order_empty_client_name(self):
        order_id = ObjectId()
        products = [Inventory(product_id=ObjectId(), name="Product A", price=9.99)]
        client = User(user_id=ObjectId(), name="", email="john.doe@example.com")
        payment = Pago(payment_id=ObjectId(), method="Efectivo", estado="pendiente")
        with self.assertRaises(ValidationError):
            Order(_id=order_id, products=products, client=client, payment=payment, 
                  order_status="pending", order_date=datetime.now(), total_price=9.99)

if __name__ == '__main__':
    unittest.main()