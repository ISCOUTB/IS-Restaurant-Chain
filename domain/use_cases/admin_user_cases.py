from domain.entities.admin import Admin
from infrastructure.repositories.admin_repository import AdminRepository

def authenticate_admin(self, admin_id: str, password: str) -> Admin:
        admin_data = self.user_repo.authenticate_admin(admin_id, password)
        if admin_data is None:
            return None
        return Admin(**admin_data)