# infrastructure/repositories/user_repository.py
import bcrypt
import uuid
from domain.entities.user import User
class UserRepository:
    def __init__(self, db):
        self.collection = db["Usuario"]

    def user_exists(self, user_id: str) -> bool:
        return self.collection.find_one({"user_id": user_id}) is not None

    def generate_unique_user_id(self) -> str:
        while True:
            user_id = str(uuid.uuid4())
            if not self.collection.find_one({"user_id": user_id}):
                return user_id

    def register_user(self, username: str, password: str, email: str) -> bool:
        user_id = self.generate_unique_user_id()
        if self.user_exists(user_id):
            return False
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {"user_id": user_id, "nombre": username, "contraseña": hashed_password, "correo": email}
        self.collection.insert_one(user_data)
        return True

    def authenticate_user(self, email: str, password: str) -> dict:
        user = self.collection.find_one({"correo": email})
        if user is None:
            return None
        stored_password = user["contraseña"]
        if not bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return None
        return {
            "user_id": user["user_id"],
            "username": user["nombre"],
            "email": user["correo"],
            "password": user["contraseña"]
        }

    def update_user(self, user_id: int, updated_user: User) -> bool:
        result = self.collection.update_one({"user_id": user_id}, {"$set": updated_user.dict()})
        return result.modified_count > 0
    
    def delete_user(self, email: str) -> None:
        self.collection.delete_one({"correo": email})

    def get_user_by_email(self, email: str) -> dict:
        user = self.collection.find_one({"correo": email})
        if user:
            return {
                "user_id": user["user_id"],
                "username": user["nombre"],
                "email": user["correo"],
                "password": user["contraseña"]
            }
        return None