import unittest
from domain.entities.user import User, UpdateUser
from interfaces.user_service import UserService
from domain.use_cases.user_use_cases import UserUseCases
from infrastructure.repositories.dbcontroller import DbController
from pydantic import ValidationError
from bson import ObjectId

class TestUserIntegration(unittest.TestCase):
    def setUp(self):
        self.db_controller = DbController()
        self.user_use_cases = UserUseCases(self.db_controller.user_repo)
        self.user_service = UserService(self.user_use_cases)

    def test_register_user_with_empty_password(self):
        with self.assertRaises(ValidationError):
            user = User(user_id="1", username="testuser", email="testuser@example.com", password="")
            self.user_service.register_user(user)

    def test_register_user_with_empty_email(self):
        with self.assertRaises(ValidationError):
            user = User(user_id="1", username="testuser", email="", password="securepassword")
            self.user_service.register_user(user)

    def test_register_user_with_empty_username(self):
        with self.assertRaises(ValidationError):
            user = User(user_id="1", username="", email="testuser@example.com", password="securepassword")
            self.user_service.register_user(user)

    def test_register_user_already_exists(self):
        user_id = ObjectId()
        user = User(user_id=str(user_id), username="testuser", email="testuser@example.com", password="securepassword")
        self.user_service.register_user(user)
        with self.assertRaises(ValidationError):
            self.user_service.register_user(user)

    def test_update_user_not_exists(self):
        updated_user = UpdateUser(username="updateduser", email="updateduser@example.com", password="newsecurepassword")
        with self.assertRaises(ValidationError):
            self.user_service.update_user("nonexistent_user_id", updated_user)

    def test_delete_user_not_found(self):
        with self.assertRaises(ValidationError):
            self.user_service.delete_user("nonexistent@example.com")

if __name__ == '__main__':
    unittest.main()