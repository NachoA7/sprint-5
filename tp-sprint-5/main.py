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
cliente1.RETIRO_EFECTIVO_CAJERO_AUTOMATICO()
cliente1.RETIRO_EFECTIVO_CAJERO_AUTOMATICO()
print(cliente1.get_transacciones())


