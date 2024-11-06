# domain/entities/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    password: str

class UpdateUser(BaseModel):
    username: Optional[str]
    email: EmailStr
    password: Optional[str]
    
