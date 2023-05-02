class nodoArbolRN(object):
    def __init__(self, info):
        self.padre = None
        self.izq = None
        self.der = None
        self.info = info
        self.color = 1
    def rotar_derecha(nodo):
        aux = nodo.izq
        nodo.izq = aux.der
        if (aux.der is not None):
            aux.der.padre = nodo
        aux.padre = nodo.padre

        if (nodo.padre is not None):
            if (nodo.padre.der == nodo):
                nodo.padre.der = aux
            else:
                nodo.padre.izq = aux
        aux.der = nodo
        nodo.padre = aux

    def rotar_izquierda(nodo):
        aux = nodo.der
        nodo.der = aux.izq
        if (aux.izq is not None):
            aux.izq.padre = nodo
        aux.padre = nodo.padre
        if (nodo.padre is not None):
            if (nodo.padre.izq == nodo):
                nodo.padre.izq = aux
            else:
                nodo.padre.der = aux
        aux.izq = nodo
        nodo.padre = aux
    def reparar_insertar(nodo):
        aux = None
        while (nodo.padre is not None and nodo.padre.color == 1):
            abuelo = nodo.padre.padre
            if (abuelo is not None and nodo.padre == nodo.padre.padre.izq):
                aux = nodo.padre.padre.der
                if (aux is not None and aux.color == 1):
                    nodo.padre.color = 0
                    aux.color = 0
                    nodo.padre.padre.color = 1
                    nodo = nodo.padre.padre
                elif (nodo == nodo.padre.der):
                    nodo = nodo.padre
                    nodoArbolRN.rotar_izquierda(nodo)
                else:
                    nodo.padre.color = 0
                    nodo.padre.padre.color = 1
                    nodoArbolRN.rotar_derecha(nodo.padre.padre)
            elif (nodo.padre.padre is not None):
                aux = nodo.padre.padre.izq
                if (aux is not None and aux.color == 1):
                    nodo.padre.color = 0
                    aux.color = 0
                    nodo.padre.padre.color = 1
                    nodo = nodo.padre.padre
                elif (nodo == nodo.padre.izq):
                    nodo = nodo.padre
                    nodoArbolRN.rotar_derecha(nodo)
                else:
                    nodo.padre.color = 0
                    nodo.padre.padre.color = 1
                    nodoArbolRN.rotar_izquierda(nodo.padre.padre)
            else:
                nodo = nodo.padre
        if (nodo.padre is None):
            nodo.color = 0
        else:
            while(nodo.padre is not None):
                nodo = nodo.padre
        return nodo
            
    
    def insertar_nodo(raiz, dato):
        ant = None
        act = raiz
        nodo = nodoArbolRN(dato)
        while (act is not None):
            ant = act
            if (nodo.info < act.info):
                act = act.izq
            else:
                act = act.der
        nodo.padre = ant
        if (ant is None):
            raiz = nodo
        elif (nodo.info < ant.info):
            ant.izq = nodo
        else:
            ant.der = nodo
        raiz = nodoArbolRN.reparar_insertar(nodo)
        return raiz