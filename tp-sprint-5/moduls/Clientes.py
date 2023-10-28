import datetime
from moduls.Functions import Funciones
import random

#Creación de la clase cliente que tiene todos los atributos y métodos de los clientes 

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
        self.dolares = 0
        self.pesos = 0

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
        self.numero_cuenta = 0
        self.tarjetas = ["VISA","MasterCard","American"]

        #Atributo transacciones que se utilizará luego para mostrarlo en el reporte
        self.transacciones = {
            "numero":f"{self.numero}",
            "nombre": f"{self.nombre}", 
            "apellido": f"{self.apellido}", 
            "dni": f"{self.dni}", 
            "tipo": f"{str(self.tipo_cliente).upper()}", 

            "transacciones":[
            ]}

        #Atributos de la clase Clientes del tipo listas
        self.tarjetas_credito = [{"numero":0,"apellido": self.apellido,"nombre":self.nombre,"monto":0,"clave":123,"tipo_de_tarjeta":""}]
        self.tarjetas_debito = [{"numero":0,"apellido": self.apellido,"nombre":self.nombre,"monto":0,"clave":123,"tipo_de_tarjeta":""}]
        self.cajas_ahorro = [{"nombre de Caja","nro","monto","moneda"}]
        self.tarjeta = [{"numero":0,"apellido":self.apellido,"nombre":self.nombre,"monto":0,"clave":123}]
        self.retiros_en_efectivo = {"Cajero 1": [0, self.cant_retiro], "Cajero 2": [0, self.cant_retiro]}
        self.comisiones = {"Salientes": self.comisiones_salientes, "Entrantes": self.comisiones_entrantes}
        self.cuenta_corriente = [{"Cuenta Corriente","Numero de cuenta corriente","Moneda","apellido","nombre"}]
        self.cuentas_de_inversion = [{"Nombre de cuenta","monto"}]
        self.chequera = [{"Nro de transaccion","motivo","apellido","nombre","monto a pagar"}]
       
    #Métodos para obtener datos

    #Retorna una lista que contiene en cada nodo un diccionario con la información de las cajas de ahorro
    def get_cajas(self):
        return self.cajas_ahorro
    
    #Retorna una lista que contiene en cada nodo un diccionario con la información de las transacciones realizadas
    def get_transacciones(self):
        return self.transacciones
    
    #Retorna una lista que contiene en cada nodo un diccionario con la información de las tarjetas de credito 
    def get_tarjetas_credito(self):
        return self.tarjetas_credito[1:]
    
    #Retorna una lista que contiene en cada nodo un diccionario con la información de las tarjetas de débito
    def get_tarjetas_debito(self):
        return self.tarjetas_debito[1:]
    
    def set_monto(self,monto):
        self.monto=monto
    

    #Procedimiento que en el caso de querer retirar un monto menor a la cantidad permitida deja el estado de la transacción 
    #como aprobada y rechada de ser el caso contrario. agrega un diccionario dentro del diccionario que esta dentro del atributo 
    #transacciones que contiene una key llamada transacciones, la cual es una lista. En la misma appendeamos el diccionario.

    def RETIRO_EFECTIVO_CAJERO_AUTOMATICO (self):
        self.monto=Funciones.descontar_comision(self.monto,self.comisiones_salientes)
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
        
        self.monto=0

    #Agus

    #Procedimiento que en el caso de querer retirar un monto menor a la cantidad permitida deja el estado de la transacción 
    #como aprobada y rechada de ser el caso contrario. agrega un diccionario dentro del diccionario que esta dentro del atributo 
    #transacciones que contiene una key llamada transacciones, la cual es una lista. En la misma appendeamos el diccionario.
    
    def RETIRO_EFECTIVO_POR_CAJA (self):
        self.monto=Funciones.descontar_comision(self.monto,self.comisiones_salientes)
        if (self.cant_retiro>self.monto):
            i=0
        else:
            i=1

        self.numero_transaccion+=1

        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "RETIRO_EFECTIVO_POR_CAJA", 
            "cuentaNumero": 2, 
            "permitidoActualParaTransccion" : self.cant_retiro , 
            "monto": self.monto, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_retiro -= self.monto

        self.monto=0
    
    def COMPRA_EN_CUOTAS_TARJETA_CREDITO_(self,tipo_tarjeta_credito):
        self.monto=Funciones.descontar_comision(self.monto,self.comisiones_salientes)
        if (self.cant_retiro_cuotas>self.monto):
            for tarjeta in self.tarjetas_credito:
                if(tarjeta["tipo_de_tarjeta"]==tipo_tarjeta_credito):
                    if(tarjeta["monto"]>self.monto):
                        i=0
                    else:
                        i=1
        else:
            i=1

        self.numero_transaccion+=1

        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i],
            "tarjeta": tipo_tarjeta_credito, 
            "tipo": "COMPRA_EN_CUOTAS_TARJETA_CREDITO_", 
            "cuentaNumero": 3, 
            "permitidoActualParaTransccion" : self.cant_retiro_cuotas, 
            "monto": self.monto, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_retiro_cuotas -= self.monto
        
        self.monto=0 

    def COMPRA_TARJETA_CREDITO_(self,tipo_tarjeta_credito):
        self.monto=Funciones.descontar_comision(self.monto,self.comisiones_salientes)
        if (self.cant_retiro_un_pago>self.monto):
            for tarjeta in self.tarjetas_credito:
                if(tarjeta["tipo_de_tarjeta"]==tipo_tarjeta_credito):
                    if(tarjeta["monto"]>self.monto):
                        i=0
                    else:
                        i=1
        else:
            i=1

        self.numero_transaccion+=1

        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i],
            "tarjeta": tipo_tarjeta_credito, 
            "tipo": "COMPRA_TARJETA_CREDITO_", 
            "cuentaNumero": 4, 
            "permitidoActualParaTransccion" : self.cant_retiro_un_pago, 
            "monto": self.monto, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_retiro_un_pago -= self.monto

        self.monto=0 

    def ALTA_TARJETA_CREDITO_(self,tipo_tarjeta_credito):
        if (self.cant_tarjetas_credito!=0 and self.tarjetas.__contains__(tipo_tarjeta_credito)):
            self.tarjetas_credito.append(
                {
                "numero":self.tarjetas_credito[-1]["numero"]+1,
                "numero_tarjeta":random.randint(100000000000,999999999999),
                "apellido":self.apellido,
                "nombre":self.nombre,
                "monto":self.monto,
                "clave":random.randint(100,999),
                "tipo_de_tarjeta":tipo_tarjeta_credito
                }
            )
            i=0
        else:
            i=1

        self.numero_transaccion+=1

        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i],
            "tarjeta": tipo_tarjeta_credito, 
            "tipo": "ALTA_TARJETA_CREDITO_", 
            "cuentaNumero": 4, 
            "permitidoActualParaTransccion" : self.cant_tarjetas_credito, 
            "monto": self.monto, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_tarjetas_credito -= 1 
        
        self.monto=0
    
    #Para el que tenga tiempo
    
    def ALTA_TARJETA_DEBITO(self):
        if (self.cant_tarjetas_debito!=0):
            self.tarjetas_debito.append(
                {
                "numero":self.tarjetas_debito[-1]["numero"]+1,
                "numero_tarjeta":random.randint(100000000000,999999999999),
                "apellido":self.apellido,
                "nombre":self.nombre,
                "monto":self.monto,
                "clave":random.randint(100,999)
                }
            )
            i=0
        else:
            i=1

        self.numero_transaccion+=1

        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i],
            "tipo": "ALTA_TARJETA_DEBITO", 
            "cuentaNumero": 5, 
            "permitidoActualParaTransccion" : self.cant_tarjetas_debito, 
            "monto": self.monto, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_tarjetas_debito -= 1

        self.monto=0

    #Seba
    def ALTA_CHEQUERA(self,monto_cheque):
        
        # #aumenta el numero de transaccion
        self.numero_transaccion+=1  
        #verifica cantidad de chequeras, si tiene disponible crea una
        if (self.cant_chequeras!=0):
            i=0
            self.chequera.append(
                {
                "Nro de transaccion":self.numero,
                "motivo": "Pago",
                "apellido":self.apellido,
                "nombre":self.nombre,
                "monto":monto_cheque,
                
                }
            )
        else:
            i=1
        
        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CHEQUERA", 
            "chequera": self.chequera,
            "chequeraDisponible": self.cant_chequeras, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_chequeras -= 1

        self.monto=0
        #fin-ALTA_CHEQUERA        

    def ALTA_CUENTA_CTE(self,tipo_moneda):
        #aumenta el numero de transaccion
        self.numero_transaccion+=1

        # verifica cantidad de cuenta, si tiene disponible crea una
        if (self.cant_cuentas_corriente!=0):
            i=0
            #verifica tipo de moneda
            if(tipo_moneda == 'Dolar'):
                self.cant_cuentas_corriente_dolares += 1
            if(tipo_moneda == 'Peso'):
                self.cant_cuentas_corriente_pesos += 1
            #creacion de cuenta corriente
            self.cuenta_corriente.append(
                {
                "Cuenta Corriente":self.cant_cuentas_corriente,
                "Numero de cuenta corriente": self.numero_cuenta,
                "Moneda": tipo_moneda,
                "apellido":self.apellido,
                "nombre":self.nombre 
                }
            )
        else:
            i=1

        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CUENTA_CTE", 
            "cuentaCorriente": self.cuenta_corriente,
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

        self.monto=0      
        #fin-ALTA_CUENTA_CTE
    
    def ALTA_CAJA_DE_AHORRO_(self,nombre_caja,tipo_moneda,monto_caja):
        #aumenta el numero de transaccion
        self.numero_transaccion+=1
        #verifica cantidad de cajas de ahorro, si tiene disponible crea una
        if (self.cant_cajas_ahorro!=0):
            i=0
            #verifica tipo de moneda
            if(tipo_moneda == 'Dolar'):
                self.cant_cajas_ahorro_dolares += 1
            if(tipo_moneda == 'Peso'):
                self.cant_cajas_ahorro_pesos += 1
            #crea la caja de ahorro 
            self.cajas_ahorro.append(
                {
                "nombre de Caja":nombre_caja,
                "nro": self.cant_cajas_ahorro,
                "monto": monto_caja,
                "moneda":tipo_moneda
                }
            )
        else:
            i=1
        
        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CAJA_DE_AHORRO_",
            "cajaAhoro":self.cajas_ahorro, 
            "cajaAhoroDisponible": self.cant_cajas_ahorro, 
            "cajaAhoroDolaresNumero": self.cant_cajas_ahorro_dolares,
            "cajaAhoroPesosNumero": self.cant_cajas_ahorro_pesos, 
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )
        if(i==0):
            self.cant_cajas_ahorro -= 1

        self.monto=0
        #fin-ALTA_CAJA_DE_AHORRO_

    def ALTA_CUENTA_DE_INVERSION(self,monto_invertir,nombre_cuenta):
        #aumenta el numero de transaccion
        self.numero_transaccion+=1
        #verifica cantidad de cajas de ahorro, si tiene disponible crea uno
        if (self.cant_cuentas_inversion!=0):
            i=0
             #crea cuenta inversion
            self.cuentas_de_inversion.append(
                {
                "Nombre de cuenta":nombre_cuenta,
                "monto": monto_invertir,
                }
            )
        else:
            i=1
        #resultado
        self.transacciones["transacciones"].append(
            {
            "estado": self.estado[i], 
            "tipo": "ALTA_CUENTA_DE_INVERSION", 
            "cuentaInvercsion":self.cuentas_de_inversion,
            "fecha": self.fecha_actual, 
            "numero": self.numero_transaccion
            }
        )

        self.monto=0
        #fin-ALTA_CAJA_DE_AHORRO_

    #Nacho
    def COMPRA_DOLAR(self, monto_dolares):
        cambio_dolar = Funciones.calcular_monto_total(monto_dolares)
        if self.cant_cajas_ahorro_pesos >= cambio_dolar:
            self.cant_cajas_ahorro_pesos -= cambio_dolar
            self.cant_cajas_ahorro_dolares += monto_dolares
            self.transacciones["transacciones"].append({
                "tipo": "COMPRA_DOLAR",
                "monto": monto_dolares,
                "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })
            return f"Compra de {monto_dolares} dólares exitosa."
        else:
            return "Saldo insuficiente en la cuenta en pesos para realizar la compra de dólares."

    def VENTA_DOLAR(self, monto_dolares):
        if self.cant_cajas_ahorro_dolares >= monto_dolares:
            self.cant_cajas_ahorro_dolares -= monto_dolares
            self.cant_cajas_ahorro_pesos += monto_dolares * 990
            self.transacciones["transacciones"].append({
                "tipo": "VENTA_DOLAR",
                "monto": monto_dolares,
                "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })
            return f"Venta de {monto_dolares} dólares exitosa."
        else:
            return "Saldo insuficiente en la cuenta en dólares para realizar la venta de dólares."

    def TRANSFERENCIA_ENVIADA_(self, tipo_moneda, beneficiario, monto):
        if tipo_moneda == "pesos":
            if self.cant_cajas_ahorro_pesos >= monto:
                self.cant_cajas_ahorro_pesos -= monto
            else:
                return "Saldo insuficiente en la cuenta en pesos para realizar la transferencia."
        elif tipo_moneda == "dolares":
            if self.cant_cajas_ahorro_dolares >= monto:
                self.cant_cajas_ahorro_dolares -= monto
            else:
                return "Saldo insuficiente en la cuenta en dólares para realizar la transferencia."
            
        beneficiario.TRANSFERENCIA_RECIBIDA_(tipo_moneda, monto)
        self.transacciones["transacciones"].append({
                "tipo": "TRANSFERENCIA_ENVIADA",
                "monto": monto,
                "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "destinatario": f"{beneficiario.apellido} {beneficiario.nombre}" 
            })
        return f"Transferencia de {monto} {tipo_moneda} exitosa hacia {beneficiario.nombre}."

    def TRANSFERENCIA_RECIBIDA_(self, tipo_moneda, monto):
        if tipo_moneda == "pesos":
            self.cant_cajas_ahorro_pesos += monto
        elif tipo_moneda == "dolares":
            self.cant_cajas_ahorro_dolares += monto
        self.transacciones["transacciones"].append({
                "tipo": "TRANSFERENCIA_RECIBIDA_",
                "monto": monto,
                "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })

    def reporte_html(self):
        i=1
        html = """<!DOCTYPE html>
        <html>
            <head>
                <html lang="es">
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                
                <title>Reportes de transferencias</title>
            </head>
            <body>
                <header>
                        <h1 class="text-light bg-dark" >Transferencias</h1>
                </header>
                <main>
                    <table class="table table-hover table-bordered table-striped table-responsive">
        """

        for transaccion in self.transacciones:
            transacciones = self.transacciones[transaccion]
            if(transacciones == []):
                transacciones = "NULL"
            if(transaccion!="transacciones"):
                html+= f"""
                    <tr>
                        <th>{transaccion}</th>
                            <td>{transacciones}</td>
                    </tr>
                    """
            else:
                html+= f"""
                    <th>{transaccion}</th>
                        <td>{transferencia}</td>
                    """

        html+="""
                    </table>
                </main>
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
            </body>
        </html>
        """        

        print("Página HTML generada con éxito.")
        
        with open('informe.html', 'w', encoding='utf-8') as file:
            file.write(html)

        file.close()

        return html
