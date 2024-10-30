import pytest
from domain.entities.inventory import Inventory
from pydantic import ValidationError

def test_create_inventory():
    inventory = Inventory(product_id=1, name="Product A", stock=100, price=9.99, description="Description of Product A")
    assert inventory.product_id == 1
    assert inventory.name == "Product A"
    assert inventory.stock == 100
    assert inventory.price == 9.99
    assert inventory.description == "Description of Product A"

def test_create_inventory_invalid_price():
    with pytest.raises(ValidationError):
        Inventory(product_id=1, name="Product A", stock=100, price="invalid-price", description="Description of Product A")

def test_create_inventory_negative_stock():
    with pytest.raises(ValidationError):
        Inventory(product_id=1, name="Product A", stock=-10, price=9.99, description="Description of Product A")

def test_create_inventory_missing_fields():
    with pytest.raises(ValidationError):
        Inventory(product_id=1, name="Product A", price=9.99, description="Description of Product A")

def test_create_inventory_empty_name():
    with pytest.raises(ValidationError):
        Inventory(product_id=1, name="", stock=100, price=9.99, description="Description of Product A")