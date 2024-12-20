# infrastructure/repositories/dbcontroller.py
from pymongo import MongoClient
from infrastructure.repositories.user_repository import UserRepository
from infrastructure.repositories.inventory_repository import InventoryRepository
from infrastructure.repositories.order_repository import OrderRepository
from infrastructure.repositories.admin_repository import AdminRepository

class DbController:
    def __init__(self):
        client = MongoClient(
            "mongodb+srv://Miche17:aumasemo32@cluster0.6ojhz7l.mongodb.net/?tls=true"
        )
        self.db = client["RestaurantChain"]
        self.user_repo = UserRepository(self.db)
        self.inventory_repo = InventoryRepository(self.db)
        self.order_repo = OrderRepository(self.db)
        self.admin_repo = AdminRepository(self.db)
