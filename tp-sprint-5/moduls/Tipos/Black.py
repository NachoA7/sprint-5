from exceptions.MaxCajaAhorro import MaxCajaAhorro

class Black:
    def __init__(self, caja_ahorro_dolares = False) -> None:
        self.__cant_tarjetas_debito = 5
        self.__caja_de_ahorro = 5
        self.__cant_cuentas_corrientes = 3
        self.__cant_extensiones = 10
        self.limite_pago=500000
        self.limite_pago_cuotas = 600000
        self.retiro_maximo = 100000
        self.limite_chequeras = 2
        self.chequeras = [[]]
        self.cuentas_inversion = []
        self.__tarjeta_Visa=[[101000111111,1]]
        self.__tarjeta_American=[[101000111111,1]]
        self.__tarjeta_MasterCard=[[101000111111,1]]
        self.__tarjeta_debito = [0000000000000000,1]
        self.__cajas_de_ahorro = [["Caja de ahorro en pesos 1", 1, 0]]
        self.__retiros_en_efectivo = {"Cajero 1": [0, 10000], "Cajero 2": [0, 10000]}
        self.__comisiones = {"Salientes": 0.1, "Entrantes": 0.05}
        if caja_ahorro_dolares:
            self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en dolares", len(self.__cajas_de_ahorro) + 1, 0])

    def getCaja(self):
        return self.__cajas_de_ahorro
    
    def agregarCaja(self):
        try:
            if len(self.__cajas_de_ahorro) <= 2:
                self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en pesos", len(self.__cajas_de_ahorro) + 1, 0])
            else:
                raise MaxCajaAhorro("No se puede agregar mas cajas de ahorro")
        except MaxCajaAhorro as e:
            print("Error: ", str(e))

    def eliminarCaja(self):
        if(len(self.__cajas_de_ahorro)>=1):
            self.__cajas_de_ahorro.remove()