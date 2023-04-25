from Arboles_binarios_AVL import NodoArbol
from Arboles_Binarios import nodoArbol
raiz = None
i = 0
pais = input("Ingrese el nombre del pais a cargar: ")
while(pais != "" and i < 21):
    raiz = NodoArbol.insertar_nodo(raiz, pais)
    i += 1
    pais = input("Ingrese el nombre del pais a cargar: ")
nodoArbol.inorden(raiz)
pais = input("Ingrese el nombre del pais a eliminar: ")
raiz, dato = nodoArbol.eliminar_nodo(raiz, pais)
if(dato is not None):
    print("El pais eliminado fue: ", dato)

pos = nodoArbol.buscar(raiz, "Argentina")
if(pos is not None):
    raiz, dato = nodoArbol.eliminar_nodo(raiz, "Argentina")
    dato = "Argentina"
    raiz = NodoArbol.insertar_nodo(raiz, dato)

nodoArbol.inorden(raiz)