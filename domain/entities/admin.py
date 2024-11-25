
from pydantic import BaseModel, Field

class Admin(BaseModel):
    admin_id: float
    username: str
    password: str = Field(..., min_length=1)