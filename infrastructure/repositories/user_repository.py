from pymongo import UpdateOne
#from domain.value_objects.email import Email 
import bcrypt
class UserRepository:
    def __init__(self, db):
        self.collection = db["Usuario"]

    def user_exists(self, username: str, email: str) -> bool:
        return self.collection.find_one({"$or": [{"nombre": username}, {"correo": email}]}) is not None


    def register_user(self, username: str, password: str, email: str) -> bool:
        if self.user_exists(username, email):
            return False
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {"nombre": username, "contraseña": hashed_password, "correo": email}
        self.collection.insert_one(user_data)
        return True

    def authenticate_user(self, email: str, password: str) -> dict:
        user = self.collection.find_one({"email": email})
        if user is None:
            return None
        # La contraseña almacenada en la base de datos ya está en bytes
        stored_password = user["password"]
        if not bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return None
        return user

    def update_usuario(self, correo: str, usuario_data: dict) -> None:
        update_operations = []
        for key, value in usuario_data.items():
            update_operations.append(UpdateOne({"email": correo}, {"$set": {key: value}}))

        if update_operations:
            self.collection.bulk_write(update_operations)

    def eliminar_usuario(self, correo: str) -> bool:
        result = self.collection.delete_one({"email": correo})
        return result.deleted_count > 0

    def get_usuario_by_nombre(self, nombre: str) -> dict:
        return self.collection.find_one({"username": nombre})

    def clear_db(self):
        self.collection.delete_many({})

    def get_user_by_email(self, email: str) -> dict:
            user = self.collection.find_one({"email": email})
            if user is None:
                print("No se encontró ningún usuario con el correo proporcionado.")
            return user