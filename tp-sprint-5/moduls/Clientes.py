import datetime
from moduls.Functions import Funciones

class Clientes:
    def  __init__(self,nombre,apellido,numero,dni,tipo_cliente) -> None:
        
        #Atributos importante
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.tipo_cliente = tipo_cliente
        self.estado = ["Aceptado","Rechazado","Pendiente"]
        self.numero_transaccion = 0
        self.monto = 0
        self.fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.fecha_anterior = 0

        #Atributos menos importantes
        self.cant_tarjetas_debito = 0
        self.cant_tarjetas_credito = 0
        self.cant_cajas_ahorro = 0
        self.cant_cajas_ahorro_dolares = 0
        self.cant_cajas_ahorro_pesos = 0
        self.cant_cuentas_corriente = 0
        self.cant_cuentas_corriente_pesos = 0 ##
        self.cant_cuentas_corriente_dolares = 0
        self.cant_cuentas_corriente_pesos = 0 ##
        self.cant_cuentas_inversion = 0
        self.cant_retiros = 0
        self.cant_retiro = 0
        self.cant_retiro_un_pago = 0
        self.cant_retiro_cuotas = 0
        self.comisiones_entrantes = 0
        self.comisiones_salientes = 0
        self.cant_chequeras = 0
        self.tarjetas = ["VISA","MasterCard","American"]

        #Atributo transacciones
        self.transacciones = {
            "numero":f"{self.numero}",
            "nombre": f"{self.nombre}", 
            "apellido": f"{self.apellido}", 
            "dni": f"{self.dni}", 
            "tipo": f"{str(self.tipo_cliente).upper()}", 

            "transacciones":[
            ]}

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
    
    def get_transacciones(self):
        return self.transacciones
    
    def RETIRO_EFECTIVO_CAJERO_AUTOMATICO (self):
        if (self.cant_retiro>self.monto):
            i=0
        else:
            i=1

        self.numero_transaccion+=1

        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", 
            "cuentaNumero": 1, 
            "permitidoActualParaTransccion" : self.cant_retiro , 
            "monto": self.monto, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_retiro -= self.monto
    #Agus
    def RETIRO_EFECTIVO_POR_CAJA (self):
        pass
    def COMPRA_EN_CUOTAS_TARJETA_CREDITO_(self,tipo_tarjeta_credito):
        pass 
    def COMPRA_TARJETA_CREDITO_(self,tipo_tarjeta_credito):
        pass 
    def ALTA_TARJETA_CREDITO_(self,tipo_tarjeta_credito):
        pass
    #Para el que tenga tiempo
    def ALTA_TARJETA_DEBITO(self):
        pass 
    #Seba
    def ALTA_CHEQUERA(self):
        #verifica cantidad de chequeras
        if (self.cant_chequeras!=0):
            i=0
        else:
            i=1
        #aumenta el numero de transaccion
        self.numero_transaccion+=1
        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CHEQUERA", 
            "chequeraDisponible": self.cant_chequeras, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_chequeras -= 1
        #fin-ALTA_CHEQUERA

    def ALTA_CUENTA_CTE(self,tipo_moneda):
        # verifica cantidad de cuentas
        if (self.cant_cuentas_corriente!=0):
            i=0
        else:
            i=1
        #verifica tipo de moneda
        if(tipo_moneda == 'Dolar'):
                self.cant_cuentas_corriente_dolares += 1
        if(tipo_moneda == 'Peso'):
                self.cant_cuentas_corriente_pesos += 1
        #aumenta el numero de transaccion
        self.numero_transaccion+=1
        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CUENTA_CTE", 
            "cuentaCorrienteDisponible": self.cant_cuentas_corriente, 
            "cuentaCorrienteDolaresNumero": self.cant_cuentas_corriente_dolares,
            "cuentaCorrientePesosNumero": self.cant_cuentas_corriente_pesos, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        #cantidad de cuentas resto 1 si se diola operacion
        if(i==0):
            self.cant_cuentas_corriente -= 1       
        #fin-ALTA_CUENTA_CTE
    
    def ALTA_CAJA_DE_AHORRO_(self,tipo_moneda):
        #verifica cantidad de cajas de ahorro
        if (self.cant_cajas_ahorro!=0):
            i=0
        else:
            i=1
        #verifica tipo de moneda
        if(tipo_moneda == 'Dolar'):
                self.cant_cajas_ahorro_dolares += 1
        if(tipo_moneda == 'Peso'):
                self.cant_cajas_ahorro_pesos += 1
        #aumenta el numero de transaccion
        self.numero_transaccion+=1
        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CAJA_DE_AHORRO_", 
            "cajaAhoroDisponible": self.cant_cajas_ahorro, 
            "cajaAhoroDolaresNumero": self.cant_cajas_ahorro_dolares,
            "cajaAhoroPesosNumero": self.cant_cajas_ahorro_pesos, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_cajas_ahorro -= 1
        #fin-ALTA_CAJA_DE_AHORRO_

    def ALTA_CUENTA_DE_INVERSION(self):
        #verifica cantidad de cajas de ahorro
        if (self.cant_cuentas_inversion!=0):
            i=0
        else:
            i=1
        #aumenta el numero de transaccion
        self.numero_transaccion+=1
        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CUENTA_DE_INVERSION", 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        #fin-ALTA_CAJA_DE_AHORRO_
    #Nacho
    def COMPRA_DOLAR(self):
        pass 
    def VENTA_DOLAR(self):
        pass
    def TRANSFERENCIA_ENVIADA_(self,tipo_moneda):
        pass 
    def TRANSFERENCIA_RECIBIDA_(self,tipo_moneda):
        pass
