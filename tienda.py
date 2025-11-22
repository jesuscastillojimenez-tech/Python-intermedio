from venta import Venta


class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ventas: list[Venta] = []

    def registrar_venta(self, venta: Venta) -> None:
        self.ventas.append(venta)
