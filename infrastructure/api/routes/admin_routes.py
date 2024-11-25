
from fastapi import APIRouter, HTTPException, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from interfaces.admin_service import AdminService
from domain.entities.admin import Admin
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.admin_user_cases import AdminUseCases

router = APIRouter()
db_controller = DbController()
admin_user_cases = AdminUseCases(db_controller.admin_repo)
admin_service = AdminService(admin_user_cases)
templates = Jinja2Templates(directory="templates")

@router.post("/login")
def login_Admin(admin_id: int = Body(...), password: str = Body(...)):
    try:
        user = admin_service.authenticate_admin(admin_id, password)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Credenciales válidas"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/loginAdmin/", response_class=HTMLResponse)
def template_loginadmin(request: Request):
    return templates.TemplateResponse("AdminLogin.html", {"request": request})

@router.get("/inventory/", response_class=HTMLResponse)
def template_inventory(request: Request):
    return templates.TemplateResponse("Inventory.html", {"request": request})
