# application/services/user_service.py
from domain.use_cases.user_use_cases import UserUseCases
from domain.entities.user import User, UpdateUser


class UserService:
    def __init__(self, user_use_cases: UserUseCases):
        self.user_use_cases = user_use_cases

    def register_user(self, user: User) -> User:
        if not user.user_id:
            raise ValueError("User ID is required")
        if not user.username:
            raise ValueError("Username is required")
        if not user.email:
            raise ValueError("Email is required")
        if not user.password:
            raise ValueError("Password is required")
        return self.user_use_cases.register_user(user)

    def authenticate_user(self, email: str, password: str) -> User:
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        return self.user_use_cases.authenticate_user(email, password)

    def update_user(self, user_id: float, updated_user: UpdateUser) -> UpdateUser:
        if not updated_user.username:
            raise ValueError("Username is required")
        if not updated_user.email:
            raise ValueError("Email is required")
        if not updated_user.password:
            raise ValueError("Password is required")
        return self.user_use_cases.update_user(user_id, updated_user)

    def delete_user(self, email: str) -> None:
        if not email:
            raise ValueError("Email is required")
        self.user_use_cases.delete_user(email)

    def get_user_by_email(self, email: str) -> User:
        if not email:
            raise ValueError("Email is required")
        return self.user_use_cases.get_user_by_email(email)