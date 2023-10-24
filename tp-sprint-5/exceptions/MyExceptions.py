class MaxCajaAhorro(Exception):
    def __init__(self, message = "No se pueden agregar mas cajas de ahorro") -> None:
        self.message = message
        super().__init__(self.message)

class OpcionNoValida(Exception):
    def __init__(self, message = "Opcion no valida. Intente nuevamente.") -> None:
        self.message = message
        super().__init__(self.message)