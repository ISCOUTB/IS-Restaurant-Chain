from typing import List
from infrastructure.repositories.user_repository import UserRepository
from domain.value_objects.email import Email
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    email: str


class MicroserviceUsuarios:
    def __init__(self, usuarios_repo: UserRepository):
        self.usuarios_repo = usuarios_repo

    def register_user(self, user: User) -> bool:
        return self.usuarios_repo.register_user(user.username, user.password, user.email)

    def authenticate_user(self, email: str, password: str) -> User:
        user_data = self.usuarios_repo.authenticate_user(email, password)
        if user_data is None:
            return None
        return User(**user_data)

    def actualizar_usuario_por_correo(self, email: str, updated_user: User) -> None:
        user_data = updated_user.dict()
        self.usuarios_repo.update_usuario(email, user_data)

    def delete_user(self, email: str) -> None:
        self.usuarios_repo.eliminar_usuario(email)

    def get_user_by_email(self, email: str) -> User:
        user_data = self.usuarios_repo.get_user_by_email(email)  # Suponiendo que este método existe en tu repositorio
        if user_data is None:
            return None
        return User(**user_data)
    
    def get_all_programacion(self) -> List[dict]:
        return self.programacion_repo.get_all_programacion()
