# application/services/user_service.py
from domain.use_cases.user_use_cases import UserUseCases
from domain.entities.user import User, UpdateUser

class UserService:
    def __init__(self, user_use_cases: UserUseCases):
        self.user_use_cases = user_use_cases

    def register_user(self, user: User) -> User:
        return self.user_use_cases.register_user(user)

    def authenticate_user(self, email: str, password: str) -> User:
        return self.user_use_cases.authenticate_user(email, password)

    def update_user(self, user_id: int, updated_user: UpdateUser) -> UpdateUser:
        return self.user_use_cases.update_user(user_id, updated_user)

    def delete_user(self, email: str) -> None:
        self.user_use_cases.delete_user(email)

    def get_user_by_email(self, email: str) -> User:
        return self.user_use_cases.get_user_by_email(email)
    

