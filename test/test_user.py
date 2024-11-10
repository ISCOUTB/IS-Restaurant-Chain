import unittest
from unittest.mock import MagicMock
from domain.entities.user import User, UpdateUser
from interfaces.user_service import UserService
from domain.use_cases.user_use_cases import UserUseCases
from pydantic import ValidationError
from bson import ObjectId

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_use_cases = MagicMock(spec=UserUseCases)
        self.user_service = UserService(self.user_use_cases)

    def test_create_user(self):
        #user_id = ObjectId()
        user = User(user_id=1, username="testuser", email="testuser@example.com", password="securepassword")
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.password, "securepassword")

    def test_add_user(self):
        #user_id = ObjectId()
        user = User(user_id=1, username="testuser", email="testuser@example.com", password="securepassword")
        self.user_use_cases.register_user.return_value = user

        result = self.user_service.register_user(user)

        self.user_use_cases.register_user.assert_called_once_with(user)
        self.assertEqual(result, user)

    def test_get_user(self):
        #user_id = ObjectId()
        user = User(user_id=1, username="testuser", email="testuser@example.com", password="securepassword")
        self.user_use_cases.get_user_by_email.return_value = user

        result = self.user_service.get_user_by_email(user.email)

        self.user_use_cases.get_user_by_email.assert_called_once_with(user.email)
        self.assertEqual(result, user)

    def test_update_user(self):
        user_id = ObjectId()
        updated_user = UpdateUser(username="updateduser", email="updateduser@example.com", password="newsecurepassword")
        self.user_use_cases.update_user.return_value = updated_user

        result = self.user_service.update_user(user_id=user_id, updated_user=updated_user)

        self.user_use_cases.update_user.assert_called_once_with(user_id=user_id, updated_user=updated_user)
        self.assertTrue(result)

    def test_delete_user(self):
        self.user_use_cases.delete_user.return_value = True

        result = self.user_service.delete_user("testuser@example.com")

        self.user_use_cases.delete_user.assert_called_once_with("testuser@example.com")
        self.assertTrue(result)

    def test_delete_user_not_found(self):
        self.user_use_cases.delete_user.return_value = False

        with self.assertRaises(Exception):
            self.user_service.delete_user("nonexistent@example.com")

        self.user_use_cases.delete_user.assert_called_once_with("nonexistent@example.com")

    def test_create_user_invalid_email(self):
        with self.assertRaises(ValidationError):
            user = User(user_id=1, username="testuser", email="", password="securepassword")
            self.user_service.register_user(user)

    def test_create_user_empty_username(self):
        with self.assertRaises(ValidationError):
            user = User(user_id=1, username="", email="testuser@example.com", password="securepassword")
            self.user_service.register_user(user)
    
    
    def test_create_user_empty_password(self):
        with self.assertRaises(ValidationError):
            user = User(user_id=1, username="testuser", email="testuser@example.com", password="")
            self.user_service.register_user(user)
            
    def test_create_user_missing_fields(self):
        with self.assertRaises(ValidationError):
            user = User(user_id=1, username="testuser", email="", password="securepassword")
            self.user_service.register_user(user)

if __name__ == '__main__':
    unittest.main()