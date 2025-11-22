from producto import Producto
from cliente import Cliente


class Venta:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def total(self) -> float:
        return sum(p.precio for p in self.productos)
