import pytest
from domain.entities.user import User
from services.user_service import UserService
from pydantic import ValidationError

def test_create_user():
    user = UserService.register_user(user_id="1", username="testuser", email="testuser@example.com", password="securepassword")
    assert user.user_id == "1"
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.password == "securepassword"

def test_create_user_invalid_email():
    with pytest.raises(ValidationError):
        UserService.register_user(user_id="1", username="testuser", email="invalid-email", password="securepassword")

def test_create_user_missing_fields():
    with pytest.raises(ValidationError):
        UserService.register_user(user_id="1", username="testuser", email=None, password="securepassword")

def test_create_user_empty_username():
    with pytest.raises(ValidationError):
        UserService.register_user(user_id="1", username="", email="testuser@example.com", password="securepassword")

def test_create_user_empty_password():
    with pytest.raises(ValidationError):
        UserService.register_user(username="testuser", email="testuser@example.com", password="")
