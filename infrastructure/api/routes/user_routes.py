# infrastructure/api/routes/user_routes.py
from fastapi import APIRouter
from interfaces.user_service import UserService
from domain.entities.user import User
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.user_use_cases import UserUseCases

router = APIRouter()

# Crear instancias necesarias para la inyección de dependencias
db_controller = DbController()
user_use_cases = UserUseCases(db_controller.user_repo)
user_service = UserService(user_use_cases)

@router.post("/register")
def register_user(user: User):
    if not user_service.register_user(user):
        return {"message": "El usuario ya existe"}
    return {"message": "Usuario registrado exitosamente"}

@router.post("/login")
def login_user(email: str, password: str):
    user = user_service.authenticate_user(email, password)
    if user is None:
        return {"message": "Credenciales incorrectas"}
    return user

@router.put("/update/{user_id}")
def update_user(user_id: int, updated_user: User):
    user_service.update_user(user_id, updated_user)
    return {"message": "Usuario actualizado exitosamente"}

@router.delete("/delete")
def delete_user(email: str):
    user_service.delete_user(email)
    return {"message": "Usuario eliminado exitosamente"}

@router.get("/get")
def get_user_by_email(email: str):
    user = user_service.get_user_by_email(email)
    if user is None:
        return {"message": "Usuario no encontrado"}
    return user