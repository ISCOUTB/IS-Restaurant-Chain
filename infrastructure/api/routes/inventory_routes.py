from fastapi import APIRouter
from fastapi import HTTPException
from interfaces.inventory_service import InventoryService
from domain.entities.inventory import Inventory
from infrastructure.repositories.dbcontroller import DbController
from domain.use_cases.inventory_use_cases import InventoryUseCases

router = APIRouter()
db_controller = DbController()
Inventory_use_cases = InventoryUseCases(db_controller.inventory_repo)
inventory_service = InventoryService(Inventory_use_cases)

@router.post("/add")
def add_inventory(inventory: Inventory):
    if not inventory_service.add_inventory(inventory):
        return {"message": "El inventario ya existe"}
    return {"message": "Inventario añadido exitosamente"}

@router.get("/get/{product_id}")
def get_inventory(product_id: int):
    inventory = inventory_service.get_inventory(product_id)
    if inventory is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return inventory

@router.put("/update/{product_id}")
def update_inventory(product_id: int, inventory: Inventory):
    if not inventory_service.update_inventory(product_id, inventory):
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return {"message": "Inventario actualizado exitosamente"}

@router.delete("/delete/{product_id}")
def delete_inventory(product_id: int):
    if not inventory_service.delete_inventory(product_id):
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return {"message": "Inventario eliminado exitosamente"}

