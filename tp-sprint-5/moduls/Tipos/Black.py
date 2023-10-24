from exceptions.MyExceptions import MaxCajaAhorro
from random import randint

class Black:
    def __init__(self, nombre, apellido, caja_ahorro_dolares = False) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.__tarjeta_debito = f"{randint(3000, 3999)} {randint(1111, 9999)} {randint(1111, 9999)} {randint(1111, 9999)}"
        self.__cajas_de_ahorro_pesos = [["pesos1", 1, 0]]
        self.__retiros_en_efectivo = {"Cajero 1": [0, 10000], "Cajero 2": [0, 10000]}
        self.__comisiones = {"Salientes": 0.1, "Entrantes": 0.05}
        if caja_ahorro_dolares:
            self.__cajas_de_ahorro_dolares = [[f"dolares1", 1, 0]]

    def getCaja(self):
        return self.__cajas_de_ahorro_pesos
    
    def agregarCajaEnPesos(self):
        try:
            if len(self.__cajas_de_ahorro_pesos) < 2:
                self.__cajas_de_ahorro_pesos.append([f"pesos{len(self.__cajas_de_ahorro_pesos) + 1}", len(self.__cajas_de_ahorro_pesos) + 1, 0])
            else:
                raise MaxCajaAhorro()
        except MaxCajaAhorro as e:
            print("Error: ", str(e))
        
    def getTarjetaDebito(self):
        return self.__tarjeta_debito