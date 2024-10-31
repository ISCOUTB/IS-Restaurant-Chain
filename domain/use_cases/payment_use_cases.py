from domain.entities.payment import Pago
from infrastructure.repositories.payment_repository import PaymentRepository

class PagoUseCases:
    def __init__(self, pago_repository: PaymentRepository):
        self.pago_repository = pago_repository

    def create_pago(self, pago: Pago) -> bool:
        return self.pago_repository.create_payment(pago)

    def get_pago(self, pago_id: int) -> Pago:
        return self.pago_repository.get_payment(pago_id)

    def update_pago(self, pago_id: int, updated_pago: Pago) -> bool:
        return self.pago_repository.update_payment(pago_id, updated_pago)

    def delete_pago(self, pago_id: int) -> None:
        self.pago_repository.delete_payment(pago_id)

    def get_pagos(self) -> list[Pago]:
        return self.pago_repository.get_payments()