class AdminRepository:
    def __init__(self, db):
        self.collection = db["Admin"]

    def authenticate_admin(self, admin_id: float, password: str) -> dict:
        admin = self.collection.find_one({"admin_id": admin_id})
        if admin is None:
            return None
        stored_password = admin["password"]
        if password != stored_password:
            return None
        return {
            "admin_id": admin["admin_id"],
            "password": admin["password"],
            "username": admin["username"],
        }

    