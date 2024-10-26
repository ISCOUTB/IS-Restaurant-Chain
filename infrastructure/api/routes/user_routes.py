from http.client import HTTPException
from os import stat
from typing import Optional
from fastapi import APIRouter, Body, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from domain.entities.user import User
from infrastructure.repositories.user_repository import UserRepository
from infrastructure.repositories.dbcontroller import DbController
from domain.entities.user import MicroserviceUsuarios

router = APIRouter(prefix="/api/v1/usuarios", tags=["Usuarios"])
dbcontroller = DbController()
service = UserRepository(dbcontroller.db)
micro = MicroserviceUsuarios(service)


@router.post("/register/")
def registrar_usuario(usuario: User):
    if not micro.register_user(usuario):
        return {"message": "El usuario ya existe"}
    return {"message": "Usuario registrado exitosamente"}