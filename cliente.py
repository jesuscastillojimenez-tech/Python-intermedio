from usuario import Usuario


class Cliente(Usuario):
    def __init__(self, nombre: str, correo: str, saldo: float):
        super().__init__(nombre, correo)
        self.saldo = saldo

    def mostrar_info(self) -> str:
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Saldo: ${self.saldo:.2f}"
