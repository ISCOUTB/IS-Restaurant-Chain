from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId

# Configuración de la base de datos
client = MongoClient("mongodb+srv://Miche17:aumasemo32@cluster0.6ojhz7l.mongodb.net/?tls=true")
db = client['RestaurantChain']
pedidos_collection = db['Pagos']

app = FastAPI()

# Modelo para el pedido
class Pedido(BaseModel):
    orderId: str
    articuloId: str
    monto: float

@app.post("/actualizar-pedido")
async def actualizar_pedido(pedido: Pedido):
    nuevo_pedido = {
        "orderId": pedido.orderId,
        "articuloId": ObjectId(pedido.articuloId),  # Convierte a ObjectId
        "monto": pedido.monto,
        "estado": "Pagado"
    }

    # Insertar el nuevo pedido en MongoDB
    result = pedidos_collection.insert_one(nuevo_pedido)
    if not result.inserted_id:
        raise HTTPException(status_code=400, detail="Error al crear el pedido")

    return {"message": "Pedido actualizado correctamente", "pedido_id": str(result.inserted_id)}

# Iniciar el servidor con el comando: uvicorn main:app --reload
