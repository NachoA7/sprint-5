from exceptions.MaxCajaAhorro import MaxCajaAhorro
from moduls.Clientes import Clientes

class Black(Clientes):
    def __init__(self,nombre,apellido,numero,dni,tipo_cliente,caja_ahorro_dolares = False) -> None:
        super().__init__(nombre,apellido,tipo_cliente,numero,dni)

        self.cant_tarjetas_debito = 5
        self.cant_tarjetas_credito = 10
        self.cant_cajas_ahorro = 5
        self.cant_cajas_ahorro_dolares = 0
        self.cant_cajas_ahorro_pesos = 0
        self.cant_cuentas_corriente = 3
        self.cant_cuentas_corriente_pesos = 0
        self.cant_cuentas_corriente_dolares = 0
        self.cant_cuentas_corriente_pesos = 0
        self.cant_cuentas_inversion = 0
        self.cant_retiros = -1
        self.cant_retiro = 100000
        self.cant_retiro_un_pago = 500000
        self.cant_retiro_cuotas = 600000
        self.comisiones_entrantes = -1
        self.comisiones_salientes = -1
        self.cant_chequeras = 2
        