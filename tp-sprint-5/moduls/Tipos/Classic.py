from moduls.Clientes import Clientes

class Classic(Clientes):
    def __init__(self,nombre,apellido,numero,dni,tipo_cliente,caja_ahorro_dolares = False) -> None:
        super().__init__(nombre,apellido,tipo_cliente,numero,dni)

        #Atributos de clientes Classic
        self.cant_tarjetas_debito = 1
        self.cant_cajas_ahorro = 1
        self.cant_cajas_ahorro_dolares = 1
        self.cant_cajas_ahorro_pesos = 1
        self.cant_retiros = 5
        self.cant_retiro = 10000
        self.comisiones_entrantes = 0.5
        self.comisiones_salientes = 1
        self.tarjetas = []
        
