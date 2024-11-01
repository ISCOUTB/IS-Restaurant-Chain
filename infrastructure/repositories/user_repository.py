# infrastructure/repositories/user_repository.py
import bcrypt
import uuid
from domain.entities.user import User
class UserRepository:
    def __init__(self, db):
        self.collection = db["Usuario"]

    def user_exists(self, user_id: str) -> bool:
        return self.collection.find_one({"user_id": user_id}) is not None

    def generate_unique_user_id(self, user_id: str = None) -> str:
        if user_id is None:
            user_id = str(uuid.uuid4())
        return bcrypt.hashpw(user_id.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def register_user(self, user_id: str,  username: str, password: str, email: str) -> User:
        user_id = self.generate_unique_user_id()
        if self.user_exists(user_id):
            return False
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {
            "user_id": user_id, 
            "username": username, 
            "email": email, 
            "password": hashed_password
        }
        self.collection.insert_one(user_data)
        return True

    def authenticate_user(self, email: str, password: str) -> dict:
        user = self.collection.find_one({"email": email})
        if user is None:
            return None
        stored_password = user["password"]
        if not bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return None
        return {
            "user_id": user["user_id"],
            "username": user["username"],
            "email": user["email"],
            "password": user["password"]
        }

    def update_user(self, user_id: str, updated_user: User) -> bool:
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": updated_user.dict()}
        )
        return result.modified_count > 0
    
    def delete_user(self, email: str) -> None:
        self.collection.delete_one({"email": email})

    def get_user_by_email(self, email: str) -> dict:
        user = self.collection.find_one({"email": email})
        if user:
            return {
                "user_id": user["user_id"],
                "username": user["username"],
                "email": user["email"],
                "password": user["password"]
            }
        return None