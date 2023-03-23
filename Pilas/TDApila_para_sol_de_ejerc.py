from pila import Pila, apilar, desapilar, pila_vacia
pdatos = Pila()
ppar = Pila()
pimpar = Pila()
dato = int(input("Ingrese un numero - 0 para salir"))

while(dato != 0):
    apilar(pdatos, dato)
    dato = int(input("Ingrese un numero - 0 para salir"))
while(not pila_vacia(pdatos)):
    dato = desapilar(pdatos)
    if(dato % 2 == 0):
        apilar(ppar, dato)
    else:
        apilar(pimpar, dato)
while(not pila_vacia(ppar)):
    dato = desapilar(ppar)
    print(dato)
while(not pila_vacia(pimpar)):
    dato = desapilar(ppar)
    print(dato)