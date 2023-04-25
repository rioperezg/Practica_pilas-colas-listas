from Arboles_binarios import nodoArbol
class NodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0
    def altura(raiz):
        if(raiz is None):
            return -1
        else:
            return raiz.altura
    def actualizaraltura(raiz):
        if(raiz is not None):
            alt_izq = NodoArbol.altura(raiz.izq)
            alt_der = NodoArbol.altura(raiz.der)
            raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1
    def rotar_simple(raiz, control):
        if control:
            aux = raiz.izq
            raiz.izq = aux.der
            aux.der = raiz
        else:
            aux = raiz.der
            raiz.der = aux.izq
            aux.izq = raiz
        NodoArbol.actualizaraltura(raiz)
        NodoArbol.actualizaraltura(aux)
        raiz = aux
        return raiz
    def rotar_doble(raiz, control):
        if control:
            raiz.izq = NodoArbol.rotar_simple(raiz.izq, False)
            raiz = NodoArbol.rotar_simple(raiz, True)
        else:
            raiz.der = NodoArbol.rotar_simple(raiz.der, True)
            raiz = NodoArbol.rotar_simple(raiz, False)
            return raiz
    def balancear(raiz):
        if(raiz is not None):
            if(NodoArbol.altura(raiz.izq)-NodoArbol.altura(raiz.der)==2):
                if(NodoArbol.altura(raiz.izq.izq)>=NodoArbol.altura(raiz.izq.der)):
                    raiz = NodoArbol.rotar_simple(raiz, True)
                else:
                    raiz = NodoArbol.rotar_doble(raiz, True)
            elif(NodoArbol.altura(raiz.der)-NodoArbol.altura(raiz.izq)==2):
                if(NodoArbol.altura(raiz.der.der)>=NodoArbol.altura(raiz.der.izq)):
                    raiz = NodoArbol.rotar_simple(raiz, False)
                else:
                    raiz = NodoArbol.rotar_doble(raiz, False)
                    return raiz
    def insertar_nodo(raiz, dato, pos):
        if(raiz is None):
            raiz = NodoArbol(dato, pos)
        elif(dato < raiz.info):
            raiz.izq = NodoArbol.insertar_nodo(raiz.izq, dato, pos)
        else:
            raiz.der = NodoArbol.insertar_nodo(raiz.der, dato, pos)
        raiz = NodoArbol.balancear(raiz)
        NodoArbol.actualizaraltura(raiz)
        return raiz
    def eliminar_nodo(raiz, clave):
        x = None
        if(raiz is not None):
            if(clave < raiz.info):
                raiz.izq, x = NodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der, x = NodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info, raiz.nrr = aux.info, aux.nrr
        raiz = NodoArbol.balancear(raiz)
        NodoArbol.actualizaraltura(raiz)
        return raiz, x
        