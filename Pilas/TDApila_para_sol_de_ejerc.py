from pila import Pila
pdatos = Pila()
ppar = Pila()
pimpar = Pila()
dato = int(input("Ingrese un numero - 0 para salir:"))

while(dato != 0):
    Pila.apilar(pdatos, dato)
    dato = int(input("Ingrese un numero - 0 para salir:"))
while(not Pila.pila_vacia(pdatos)):
    dato = Pila.desapilar(pdatos)
    if(dato % 2 == 0):
        Pila.apilar(ppar, dato)
    else:
        Pila.apilar(pimpar, dato)
while(not Pila.pila_vacia(ppar)):
    dato = Pila.desapilar(ppar)
    print(dato)
while(not Pila.pila_vacia(pimpar)):
    dato = Pila.desapilar(ppar)
    print(dato)