from moduls.Clientes import Clientes

class Classic(Clientes):
    def __init__(self,nombre,apellido,numero,dni,tipo_cliente,caja_ahorro_dolares = False) -> None:
        super().__init__(nombre,apellido,tipo_cliente,numero,dni)

        self.cant_tarjetas_debito = 1
        self.cant_cajas_ahorro = 1
        self.cant_cajas_ahorro_dolares = 1
        self.cant_cajas_ahorro_pesos = 1
        self.cant_retiros = 5
        self.cant_retiro = 10000
        self.comisiones_entrantes = 0.05
        self.comisiones_salientes = 0.1
        self.tarjetas = []

        # if caja_ahorro_dolares:
        #     self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en dolares", len(self.__cajas_de_ahorro) + 1, 0])

    # def getCaja(self):
    #     return self.__cajas_de_ahorro
    
    # def agregarCaja(self):
    #     try:
    #         if len(self.__cajas_de_ahorro) <= 1:
    #             self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en pesos", len(self.__cajas_de_ahorro) + 1, 0])
    #         else:
    #             raise MaxCajaAhorro("No se puede agregar mas cajas de ahorro")
    #     except MaxCajaAhorro as e:
    #         print("Error: ", str(e))

    # def eliminarCaja(self):
    #     if len(self.__cajas_de_ahorro)==1:
    #         self.__cajas_de_ahorro.remove()
        
