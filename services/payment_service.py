# application/services/Pago_service.py
from domain.entities.payment import Pago
from domain.use_cases.payment_use_cases import PagoUseCases


class PagoService:
    def __init__(self, pago_use_cases: PagoUseCases):
        self.pago_use_cases = pago_use_cases

    def create_pago(self, pago: Pago) -> bool:
        """
        Crea un nuevo pago.

        :param pago: El pago a crear.
        :return: True si el pago se creó con éxito, False en caso contrario.
        """
        return self.pago_use_cases.create_pago(pago)

    def get_pago(self, pago_id: int) -> Pago:
        """
        Obtiene un pago por su ID.

        :param pago_id: El ID del pago a obtener.
        :return: El pago con el ID especificado.
        """
        return self.pago_use_cases.get_pago(pago_id)

    def update_pago(self, pago_id: int, updated_pago: Pago) -> bool:
        """
        Actualiza un pago.

        :param pago_id: El ID del pago a actualizar.
        :param updated_pago: El pago actualizado.
        :return: True si el pago se actualizó con éxito, False en caso contrario.
        """
        return self.pago_use_cases.update_pago(pago_id, updated_pago)

    def delete_pago(self, pago_id: int) -> None:
        """
        Elimina un pago.

        :param pago_id: El ID del pago a eliminar.
        """
        self.pago_use_cases.delete_pago(pago_id)

    def get_pagos(self) -> list[Pago]:
        """
        Obtiene todos los pagos.

        :return: Una lista de pagos.
        """
        return self.pago_use_cases.get_pagos()