from bson import ObjectId

class Pago:
    def __init__(self, _id, clienteId, monto, metodoPago, estado, fechaPago):
        self._id = ObjectId(_id)
        self.clienteId = ObjectId(clienteId)
        self.monto = monto
        self.metodoPago = metodoPago
        self.estado = estado
        self.fechaPago = fechaPago