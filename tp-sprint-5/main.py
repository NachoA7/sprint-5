from moduls.Tipos.Classic import *
from moduls.Tipos.Gold import *
from moduls.Tipos.Black import *
from exceptions.MyExceptions import OpcionNoValida

while True:
    try:
        tipoCliente = str(input("Ingrese la opción adecuada para usted:\n1. Classic\n2. Gold\n3. Black\n"))
        if (tipoCliente == 1) or (tipoCliente.lower() == "classic"):
            cl1 = Classic("Nombre", "Apellido", True)
            break
        elif (tipoCliente == 2) or (tipoCliente.lower() == "gold"):
            cl1 = Gold("Nombre", "Apellido", True)
            break
        elif (tipoCliente == 2) or (tipoCliente.lower() == "black"):
            cl1 = Black("Nombre", "Apellido", True)
            break
        else:
            raise OpcionNoValida()
    except OpcionNoValida as e:
        print(f"\nError: {str(e)}\n")

cl2 = Classic("Nombre", "Apellido", True)

print(cl2.getCaja())
cl2.agregarCajaEnPesos()
print(cl2.getCaja())
cl2.agregarCajaEnPesos()
print(cl2.getCaja())
print(cl2.getTarjetaDebito())