from enums.tipoproducto import TipoProducto 

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int, tipo: TipoProducto):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo 

    def mostrar(self):
        if self.tipo == TipoProducto.PAN:
            return "Pan"
        elif self.tipo == TipoProducto.BEBIDA:
            return "Bebida"
        elif self.tipo == TipoProducto.SNACK:
            return "Snack"
        else:
            return "Otro"