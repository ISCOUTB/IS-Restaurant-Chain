# infrastructure/repositories/dbcontroller.py
from pymongo import MongoClient
from infrastructure.repositories.user_repository import UserRepository

class DbController:
    def __init__(self):
        client = MongoClient("mongodb+srv://Miche17:aumasemo32@cluster0.6ojhz7l.mongodb.net/?tls=true")
        self.db = client["RestaurantChain"]
        self.user_repo = UserRepository(self.db)