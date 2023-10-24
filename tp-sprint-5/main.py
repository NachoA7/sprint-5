from moduls.Clientes import Clientes
from moduls.Tipos.Classic import Classic
from moduls.Tipos.Gold import Gold
from moduls.Tipos.Black import Black
import sys

cliente1 = Clientes("Agustin","Corro Molas","Gold")

if(cliente1.tipo=='classic'):
    cliente1 = Classic(cliente1.nombre,cliente1.apellido,cliente1.tipo,False)
elif(cliente1.tipo.lower()=='gold'):
    cliente1 = Gold(cliente1.nombre,cliente1.apellido,cliente1.tipo,False)
elif(cliente1.tipo.lower()=='black'):
    cliente1 = Black(cliente1.nombre,cliente1.apellido,cliente1.tipo,False)

cliente1.agregarCaja(5,"pesos")
cliente1.agregarCaja(10,"dolares")
cliente1.agregarCaja(15,"Pesos")
print(cliente1.get_cajas())
cliente1.eliminarCaja(0)
print(cliente1.get_cajas())
