from exceptions.MaxCajaAhorro import MaxCajaAhorro

class Gold:
    def __init__(self, caja_ahorro_dolares = False) -> None:
        self.__cant_cajas_de_ahorro = 2
        self.__cant_cuenta_corrientes = 1
        self.__limite_pago = 150000
        self.__limite_pago_cuotas = 100000
        self.__max_retiros = 20000
        self.__cuentas_de_inversion = [[0]]
        self.__chequera = [[]]
        self.__tarjeta_visa = [0000000000000000,1,4]
        self.__tarjeta_masterCard = [0000000000000000,1,4]
        self.__tarjeta_debito = 000000000000000
        self.__cajas_de_ahorro = [["Caja de ahorro en pesos 1", 1, 0]]
        self.__cuenta_corriente = [["Cuenta Corriente",1]]
        self.__retiros_en_efectivo = {"Cajero 1": [0, 10000], "Cajero 2": [0, 10000]}
        self.__comisiones = {"Salientes": 0.05, "Entrantes": 0.01}
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