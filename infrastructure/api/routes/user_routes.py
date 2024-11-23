from fastapi import APIRouter, HTTPException, Body
from interfaces.user_service import UserService
from domain.entities.user import User, UpdateUser
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.user_use_cases import UserUseCases
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
db_controller = DbController()
user_use_cases = UserUseCases(db_controller.user_repo)
user_service = UserService(user_use_cases)
user = Jinja2Templates(directory="templates")



@router.post("/register")
def register_user(user: User):
    try:
        user_service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Usuario registrado exitosamente"}


@router.post("/login")
def login_user(email: str = Body(...), password: str = Body(...)):
    try:
        user = user_service.authenticate_user(email, password)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Credenciales válidas"}
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
    
@router.get("/register/", response_class=HTMLResponse)
def template_register(request: Request):
    return user.TemplateResponse("Signup.html", {"request": request})

@router.get("/login/", response_class=HTMLResponse)
def template_login(request: Request):
    return user.TemplateResponse("Login.html", {"request": request})

@router.get("/home_login/", response_class=HTMLResponse)
def template_home_login(request: Request):
    return user.TemplateResponse("HomeLogin.html", {"request": request})
