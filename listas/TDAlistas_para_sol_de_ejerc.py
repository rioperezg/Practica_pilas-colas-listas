from listas import listas
lista = listas.Lista()
dato = input("Ingrese una palabra")
while(dato != ""):
    listas.Lista.insertar(lista, dato)
    dato = input("ingrese una palabra")
buscado = input("Ingrese la palabra a buscar")
posicion = listas.Lista.buscar(lista, buscado)
if(posicion is not None):
    dato = listas.Lista.eliminar(lista, posicion.info)
    print("Elemento eliminado: ", dato)
else:
    print("No se encontro el elemento a eliminar")
listas.Lista.barrido(lista)