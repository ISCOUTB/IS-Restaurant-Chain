# domain/entities/user.py
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    password: str