class nodoLista(object):
    info, sig = None, None
class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
    def insertar(lista, dato):
        nodo = nodoLista()
        nodo.info = dato
        if (lista.inicio is None) or (lista.inicio.info > dato):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while(act is not None and act.info < dato):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamaño += 1
    def lista_vacia(lista):
        return lista.inicio is None
    def eliminar(lista, clave):
        dato = None
        if(lista.inicio.info == clave):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamaño -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while(actual is not None and actual.info != clave):
                anterior = anterior.sig
                actual = actual.sig
            if (actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamaño -= 1
        return dato
    def tamaño(lista):
        return lista.tamaño
    def buscar(lista, buscando):
        aux = lista.inicio
        while(aux is not None and aux.info != buscando):
            aux = aux.sig
        return aux
    def barrido(lista):
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig