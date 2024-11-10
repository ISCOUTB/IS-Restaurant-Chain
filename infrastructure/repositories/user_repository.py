from domain.entities.user import User, UpdateUser
from pydantic import EmailStr


class UserRepository:
    def __init__(self, db):
        self.collection = db["Usuario"]

    def user_exists(self, user_id: float) -> bool:
        return self.collection.find_one({"user_id": user_id}) is not None

    def username_exists(self, username: str) -> bool:
        return self.collection.find_one({"username": username}) is not None

    def email_exists(self, email: EmailStr) -> bool:
        return self.collection.find_one({"email": email}) is not None

    def register_user(self, user_id: float, username: str, email: str, password: str) -> bool:
        user_data = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "password": password
        }
        self.collection.insert_one(user_data)
        return True

    def authenticate_user(self, email: str, password: str) -> dict:
        user = self.collection.find_one({"email": email})
        if user is None:
            return None
        stored_password = user["password"]
        if password != stored_password:
            return None
        return {
            "user_id": user["user_id"],
            "username": user["username"],
            "email": user["email"],
            "password": user["password"]
        }

    def update_user(self, user_id: float, updated_user: UpdateUser) -> bool:
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