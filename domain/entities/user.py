# domain/entities/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    password: str = Field(..., min_length=1)
class UpdateUser(BaseModel):
    username: Optional[str]
    email: EmailStr
    password: str = Field(..., min_length=1)
    
