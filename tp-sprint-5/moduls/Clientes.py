class Clientes:
    def  __init__(self,nombre,apellido,tipo) -> None:
        
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
        self.cant_tarjetas_debito = 0
        self.cant_tarjetas_credito = 0
        self.cant_cajas_ahorro = 0
        self.cant_cajas_ahorro_dolares = 0
        self.cant_cajas_ahorro_pesos = 0
        self.cant_cuentas_corriente = 0
        self.cant_cuentas_corriente_pesos = 0
        self.cant_cuentas_corriente_dolares = 0
        self.cant_cuentas_corriente_pesos = 0
        self.cant_cuentas_inversion = 0
        self.cant_retiros = 0
        self.cant_retiro = 0
        self.cant_retiro_un_pago = 0
        self.cant_retiro_cuotas = 0
        self.comisiones_entrantes = 0
        self.comisiones_salientes = 0
        self.cant_chequeras = 0
        self.tarjetas = ["VISA","MasterCard","American"]

        self.tarjetas_credito = [["Número",self.apellido,self.nombre,"monto","clave"]]
        self.tarjetas_debito = [["Número",self.apellido,self.nombre,"monto","tipo de tarjeta","clave"]]
        self.cajas_ahorro = [["Nombre de Caja","nro","monto","moneda"]]
        self.tarjeta = [["Número",self.apellido,self.nombre,"monto","clave"]]
        self.retiros_en_efectivo = {"Cajero 1": [0, self.cant_retiro], "Cajero 2": [0, self.cant_retiro]}
        self.comisiones = {"Salientes": self.comisiones_salientes, "Entrantes": self.comisiones_entrantes}
        self.cuenta_corriente = [["Cuenta Corriente","Numero de cuenta corriente"]]
        self.cuentas_de_inversion = [["Nombre de cuenta","monto"]]
        self.chequera = [["Nro de transaccion","motivo","monto a pagar"]]


    def agregarCaja(self,monto,moneda):
        moneda = moneda.title()
        if(len(self.cajas_ahorro)<=self.cant_cajas_ahorro and (moneda=="Pesos" or moneda=="Dolares")):
            self.cajas_ahorro.append([f"Caja de ahorro {len(self.cajas_ahorro)} en {moneda}",len(self.cajas_ahorro),monto,moneda])

    def eliminarCaja(self,nroCaja):
        if(len(self.cajas_ahorro)>0 and 0<nroCaja and nroCaja<=len(self.cajas_ahorro)):
            self.cajas_ahorro.pop(nroCaja)
        
    def get_cajas(self):
        return self.cajas_ahorro