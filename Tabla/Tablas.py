from lista import listas

# def function"1" - tabla hash cerrada, mientras que def function"2" - tabla hash encadenada
def crear_tabla(tamaño):
    tabla = [None] * tamaño
def cantidad_elementos1(tabla):
    return len(tabla) - tabla.count(None)
def cantidad_elementos2(tabla):
    return sum(listas.Lista.tamaño(lista) for lista in tabla if lista is not None)
def funcion_hash(dato, tamaño_tabla):
    return len(str(dato).strip()) % tamaño_tabla
def agregar1(tabla, dato):
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is None):
        tabla[posicion] = listas.Lista()  
    listas.Lista.insertar(tabla[posicion], dato)
def agregar2(tabla, dato):
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is None):
        tabla[posicion] = dato
    else:
        print("Se produjo una colision")
# def buscar1(tabla, buscado):
    # pos = None
    # posicion = funcion_hash(buscado, len(tabla))
    # if(tabla[posicion] is not None):
        # pos =....NO SE ENCUENTRA LA FUNCION BUSQUEDA
def buscar2(tabla, buscado):
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if(tabla[posicion] is not None):
        if(buscado == tabla[posicion]):
            pos = posicion
        else:
            print("aplicar funcion de sondeo")
    return pos
def quitar1(tabla, dato):
    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is not None):
        if(dato == tabla[posicion]):
            dato = tabla[posicion]
            tabla[posicion] = None
        else:
            print("Aplicar funcion de sondeo")
    return dato

def quitar2(tabla, dato):
    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is not None):
        dato = listas.Lista.eliminar(tabla[posicion], dato)
        if(listas.Lista.lista_vacia(tabla[posicion])):
            tabla[posicion] = None
    return dato