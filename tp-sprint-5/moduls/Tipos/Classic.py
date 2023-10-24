from exceptions.MaxCajaAhorro import MaxCajaAhorro

class Classic:
    def __init__(self, caja_ahorro_dolares = False) -> None:
        self.cant_cajas = 1
        self.cant_tarjetas = 1
        self.limite_retiros = 5
        self.limite_extraccion = 10000
        self.__tarjeta_visa = [00000000000000,1]
        self.__tarjeta_masterCard = [00000000000000,1]
        self.__cajas_de_ahorro = [["Caja de ahorro en pesos 1", 1, 0]]
        self.__retiros_en_efectivo = {"Cajero 1": [0, 10000], "Cajero 2": [0, 10000]}
        self.__comisiones = {"Salientes": 0.1, "Entrantes": 0.05}
        if caja_ahorro_dolares:
            self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en dolares", len(self.__cajas_de_ahorro) + 1, 0])

    def getCaja(self):
        return self.__cajas_de_ahorro
    
    def agregarCaja(self):
        try:
            if len(self.__cajas_de_ahorro) <= 1:
                self.__cajas_de_ahorro.append([f"Caja de ahorro {len(self.__cajas_de_ahorro) + 1} en pesos", len(self.__cajas_de_ahorro) + 1, 0])
            else:
                raise MaxCajaAhorro("No se puede agregar mas cajas de ahorro")
        except MaxCajaAhorro as e:
            print("Error: ", str(e))

    def eliminarCaja(self):
        if len(self.__cajas_de_ahorro)==1:
            self.__cajas_de_ahorro.remove()
        
