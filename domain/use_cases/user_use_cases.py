# domain/use_cases/user_use_cases.py
from domain.entities.user import User
from infrastructure.repositories.user_repository import UserRepository

class UserUseCases:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, user: User) -> bool:
        return self.user_repo.register_user(user.username, user.password, user.email)

    def authenticate_user(self, email: str, password: str) -> User:
        user_data = self.user_repo.authenticate_user(email, password)
        if user_data is None:
            return None
        return User(**user_data)

    def update_user(self, email: str, updated_user: User) -> None:
        user_data = updated_user.dict()
        self.user_repo.update_user(email, user_data)

    def delete_user(self, email: str) -> None:
        self.user_repo.delete_user(email)

    def get_user_by_email(self, email: str) -> User:
        user_data = self.user_repo.get_user_by_email(email)
        if user_data is None:
            return None
        return User(**user_data)