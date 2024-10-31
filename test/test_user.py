import unittest
from domain.entities.user import User
from interfaces.user_service import UserService
from pydantic import ValidationError

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        user = UserService.register_user(user_id="1", username="testuser", email="testuser@example.com", password="securepassword")
        self.assertEqual(user.user_id, "1")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.password, "securepassword")

    def test_create_user_invalid_email(self):
        with self.assertRaises(ValidationError):
            UserService.register_user(user_id="1", username="testuser", email="invalid-email", password="securepassword")

    def test_create_user_missing_fields(self):
        with self.assertRaises(ValidationError):
            UserService.register_user(user_id="1", username="testuser", email=None, password="securepassword")

    def test_create_user_empty_username(self):
        with self.assertRaises(ValidationError):
            UserService.register_user(user_id="1", username="", email="testuser@example.com", password="securepassword")

    def test_create_user_empty_password(self):
        with self.assertRaises(ValidationError):
            UserService.register_user(username="testuser", email="testuser@example.com", password="")
    
if __name__ == '__main__':
    unittest.main()
