from fastapi import APIRouter, HTTPException
from interfaces.user_service import UserService
from domain.entities.user import User, UpdateUser
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.user_use_cases import UserUseCases

router = APIRouter()
db_controller = DbController()
user_use_cases = UserUseCases(db_controller.user_repo)
user_service = UserService(user_use_cases)


@router.post("/register")
def register_user(user: User):
    try:
        user_service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Usuario registrado exitosamente"}


@router.post("/login")
def login_user(email: str, password: str):
    try:
        user = user_service.authenticate_user(email, password)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/update/{user_id}")
def update_user(user_id: float, updated_user: UpdateUser):
    try:
        user_service.update_user(user_id, updated_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Usuario actualizado exitosamente"}


@router.delete("/delete")
def delete_user(email: str):
    try:
        user_service.delete_user(email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Usuario eliminado exitosamente"}


@router.get("/get")
def get_user_by_email(email: str):
    try:
        user = user_service.get_user_by_email(email)
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))