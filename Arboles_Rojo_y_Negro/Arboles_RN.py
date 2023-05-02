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
    def eliminar_nodo(raiz, clave):
        if ( y.padre is not None):
            if(y.padre.izq is not None and y.padre.izq == y):
                y.padre.izq = x
            elif(y.padre.der is not None and y.padre.der == y):
                y.padre.der = x
        if(x is None and y.padre is not None and y.color == o):
            x = nodoArbolRN(0)
            x.color = y.color
        if(x is not None):
            x.padre = y.padre
        if (y != aux):
            aux.info = y.info
        if (y.padre is None and y.izq is None and y.der is None):
            raiz = x
            return raiz, dato
        if (y.color == 0):
            aux = nodoArbolRN.reparar_eliminar(x)
        if (aux is not None):
            raiz = aux
        # return raiz, dato
    # eliminacion con reparacion
        while (nodo is not None and nodo.padre is not None and nodo.color == 0):
            if (nodo == nodo.padre.izq or nodo.padre.izq is None):
                w = nodo.padre.der
                if (w.color == 1):
                    w.color = 0
                    nodo.padre.color = 1
                    nodoArbolRN.rotar_izquierda(nodo.padre)
                    w = nodo.padre.der
                if (w.izq is None and w.der is None) or (w.izq is not None and 
                    w.izq.color == 0 and w.der is not None and w.der.color == 0):
                    w.color = 1
                    nodo = nodo.padre
                else:
                    if(w.der.color == 0):
                        w.izq.color = 0
                        w.color = 1
                        nodoArbolRN.rotar_derecha(w)
                        w = nodo.padre.der
                    w.color = nodo.padre.color
                    nodo.padre.color = 0
                    w.der.color = 0
                    nodoArbolRN.rotar_izquierda(nodo.padre)

        