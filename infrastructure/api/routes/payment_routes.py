from fastapi import APIRouter, FastAPI
from services.payment_service import PagoService
from domain.entities.payment import Pago
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.payment_use_cases import PagoUseCases

router = APIRouter()

# Ruta para crear un nuevo pago
@router.post("/payments/")
async def create_payment(payment: Pago):
    payment_service = PagoService(PagoUseCases(DbController()))
    return {"message": "Pago creado con éxito", "data": payment_service.create_pago(payment.dict())}


# Ruta para obtener todos los pagos
@router.get("/payments/")
async def get_payments():
    payment_service = PagoService(PagoUseCases(DbController()))
    return {"message": "Pagos obtenidos con éxito", "data": payment_service.get_pagos()}


# Ruta para obtener un pago por ID
@router.get("/payments/{id}")
async def get_payment(id: str):
    payment_service = PagoService(PagoUseCases(DbController()))
    return {"message": "Pago obtenido con éxito", "data": payment_service.get_pago(id)}


# Ruta para actualizar un pago
@router.put("/payments/{id}")
async def update_payment(id: str, payment: Pago):
    payment_service = PagoService(PagoUseCases(DbController()))
    return {"message": "Pago actualizado con éxito", "data": payment_service.update_pago(id, payment.dict())}


# Ruta para eliminar un pago
@router.delete("/payments/{id}")
async def delete_payment(id: str):
    payment_service = PagoService(PagoUseCases(DbController()))
    return {"message": "Pago eliminado con éxito", "data": payment_service.delete_pago(id)}