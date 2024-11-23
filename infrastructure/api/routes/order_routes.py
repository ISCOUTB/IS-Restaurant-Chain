from fastapi import APIRouter, HTTPException
from bson import ObjectId
from domain.entities.order import Order
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.order_use_cases import OrderUseCases

router = APIRouter()
db_controller = DbController()
order_use_cases = OrderUseCases(db_controller.order_repo)

@router.post("/addOrder")
def add_order(order: Order):
    created_order = order_use_cases.add_order(order)
    if not created_order:
        raise HTTPException(status_code=400, detail="Error al crear el pedido")
    return {"message": "Pedido añadido exitosamente", "order": created_order}

@router.get("/getOrder/{order_id}")
def get_order(order_id: str):
    order = order_use_cases.get_order(ObjectId(order_id))
    if order is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order

@router.put("/updateOrder/{order_id}")
def update_order(order_id: str, order: Order):
    if not order_use_cases.update_order(ObjectId(order_id), order):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"message": "Pedido actualizado exitosamente"}

@router.delete("/deleteOrder/{order_id}")
def delete_order(order_id: str):
    if not order_use_cases.delete_order(ObjectId(order_id)):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"message": "Pedido eliminado exitosamente"}

@router.put("/add_product/{order_id}")
def add_product_to_order(order_id: str, product_id: int):
    if not order_use_cases.add_product_to_order(ObjectId(order_id), product_id):
        raise HTTPException(status_code=404, detail="Pedido no encontrado o producto no añadido")
    return {"message": "Producto añadido al pedido exitosamente"}

@router.put("/remove_product/{order_id}/{product_id}")
def remove_product_from_order(order_id: str, product_id: int):
    if not order_use_cases.remove_product_from_order(ObjectId(order_id), product_id):
        raise HTTPException(status_code=404, detail="Pedido no encontrado o producto no eliminado")
    return {"message": "Producto eliminado del pedido exitosamente"}

@router.put("/cancelOrder/{order_id}")
def cancel_order(order_id: str):
    if not order_use_cases.cancel_order(ObjectId(order_id)):
        raise HTTPException(status_code=404, detail="Pedido no encontrado o no se pudo cancelar")
    return {"message": "Pedido cancelado exitosamente"}

@router.put("/pay/{order_id}")
def pay_order(order_id: str):
    if not order_use_cases.pay_order(ObjectId(order_id)):
        raise HTTPException(status_code=404, detail="Pedido no encontrado o no se pudo pagar")
    return {"message": "Pedido pagado exitosamente"}