# application/services/user_service.py
from domain.use_cases.admin_user_cases import AdminUseCases
from domain.entities.admin import Admin

class AdminService: 
    def __init__(self, AdminUseCases: AdminUseCases):
        self.AdminUseCases = AdminUseCases
        
    def authenticate_admin(self, admin_id: int, password: str) -> Admin:
        if not admin_id:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        return self.AdminUseCases.authenticate_admin(admin_id, password)