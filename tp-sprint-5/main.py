from moduls.Clientes import Clientes
from moduls.Tipos.Classic import Classic
from moduls.Tipos.Gold import Gold
from moduls.Tipos.Black import Black

cliente1 = Clientes("Agustin","Corro Molas",100000,42932897,"Gold")

if(cliente1.tipo_cliente=='classic'):
    cliente1 = Classic(cliente1.nombre,cliente1.apellido,cliente1.numero,cliente1.dni,cliente1.tipo_cliente,False)
elif(cliente1.tipo_cliente.lower()=='gold'):
    cliente1 = Gold(cliente1.nombre,cliente1.apellido,cliente1.numero,cliente1.dni,cliente1.tipo_cliente,False)
elif(cliente1.tipo_cliente.lower()=='black'):
    cliente1 = Black(cliente1.nombre,cliente1.apellido,cliente1.numero,cliente1.dni,cliente1.tipo_cliente,False)

# cliente1.agregarCaja(5,"pesos")
# cliente1.agregarCaja(10,"dolares")
# cliente1.agregarCaja(15,"Pesos")
# print(cliente1.get_cajas())
# cliente1.eliminarCaja(0)
# print(cliente1.get_cajas())

# cliente1.RETIRO_EFECTIVO_CAJERO_AUTOMATICO()
# cliente1.RETIRO_EFECTIVO_CAJERO_AUTOMATICO()
# print(cliente1.get_transacciones())

# cliente1.ALTA_TARJETA_CREDITO_("VISA")
# cliente1.RETIRO_EFECTIVO_POR_CAJA()
# cliente1.COMPRA_EN_CUOTAS_TARJETA_CREDITO_("VISA")
# cliente1.COMPRA_TARJETA_CREDITO_("VISA")
# cliente1.ALTA_TARJETA_DEBITO()
# print(cliente1.get_transacciones())
# print("-------")
# print("Tarjetas")
# print("-------")
# print("Credito")
# print(cliente1.get_tarjetas_credito())
# print("Debito")
# print(cliente1.get_tarjetas_debito())

# cliente1.ALTA_CHEQUERA(1000)
# cliente1.ALTA_CUENTA_CTE("Dolares")
# cliente1.ALTA_CAJA_DE_AHORRO_("caja2","Pesos",20000)
# cliente1.ALTA_CUENTA_DE_INVERSION(20000,"acciones")
# print(cliente1.get_transacciones())

# cliente1.set_monto(1000)
# cliente1.COMPRA_DOLAR()
# cliente1.set_monto(500)
# cliente1.VENTA_DOLAR()
# cliente1.set_monto(500)
# cliente1.TRANSFERENCIA_RECIBIDA_("pesos")
# cliente1.set_monto(100)
# cliente1.TRANSFERENCIA_ENVIADA_("pesos")

#print(cliente1.get_transacciones())

print(cliente1.reporte_html())
