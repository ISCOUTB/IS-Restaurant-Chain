from domain.entities.user import User, UpdateUser
from infrastructure.repositories.user_repository import UserRepository

class UserUseCases:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, user: User) -> User:
        if not self.user_repo.user_exists(user.user_id):
            raise ValueError("User ID exists")
        if not self.user_repo.username_exists(user.username):
            raise ValueError("Username exists")
        if not self.user_repo.email_exists(user.email):
            raise ValueError("Email exists")
        return self.user_repo.register_user(user.user_id,
                                            user.username, 
                                            user.password, 
                                            user.email)

    def authenticate_user(self, email: str, password: str) -> User:
        user_data = self.user_repo.authenticate_user(email, password)
        if user_data is None:
            return None
        return User(**user_data)

    def update_user(self, user_id: str, updated_user: UpdateUser) -> UpdateUser:
        if not self.user_repo.user_exists(user_id):
            raise ValueError("User does not exist")
        return self.user_repo.update_user(user_id, updated_user)

    def delete_user(self, email: str) -> None:
        user = self.user_repo.get_user_by_email(email)
        if user is None:
            raise ValueError("User not found")
        self.user_repo.delete_user(email)

    def get_user_by_email(self, email: str) -> User:
        user_data = self.user_repo.get_user_by_email(email)
        if user_data is None:
            return None
        return User(**user_data)