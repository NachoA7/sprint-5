from exceptions.MaxCajaAhorro import MaxCajaAhorro
from moduls.Clientes import Clientes

class Gold(Clientes):
    def __init__(self,nombre,apellido,numero,dni,tipo_cliente, caja_ahorro_dolares = False) -> None:
        super().__init__(nombre,apellido,numero,dni,tipo_cliente)
        
        self.cant_tarjetas_debito = 1
        self.cant_tarjetas_credito = 5
        self.cant_cajas_ahorro = 2
        self.cant_retiros = -1
        self.cant_retiro = 20000
        self.cant_retiro_un_pago = 150000
        self.cant_retiro_cuotas = 100000
        self.comisiones_entrantes = 0.1
        self.comisiones_salientes = 0.5
        self.cant_chequeras = 1
        self.tarjetas = ["VISA","MasterCard"]