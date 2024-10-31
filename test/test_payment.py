import pytest
from domain.entities.payment import Pago
from services.payment_service import PagoService
from pydantic import ValidationError


def test_create_pago():
    pago = PagoService.create_pago(pago_id="1", amount=100, payment_method="tarjeta")
    assert pago.pago_id == "1"
    assert pago.amount == 100
    assert pago.payment_method == "tarjeta"


def test_create_pago_invalid_amount():
    with pytest.raises(ValidationError):
        PagoService.create_pago(pago_id="1", amount=-100, payment_method="tarjeta")


def test_create_pago_missing_fields():
    with pytest.raises(ValidationError):
        PagoService.create_pago(pago_id="1", amount=100, payment_method=None)


def test_create_pago_empty_payment_method():
    with pytest.raises(ValidationError):
        PagoService.create_pago(pago_id="1", amount=100, payment_method="")


def test_create_pago_invalid_payment_method():
    with pytest.raises(ValidationError):
        PagoService.create_pago(pago_id="1", amount=100, payment_method="invalid-method")