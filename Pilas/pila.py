from pila import Pila, apilar, desapilar, pila_vacia
class nodoPila(object):
    info, sig = None, None
class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamaño = 0
    def apilar(pila, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.tamaño += 1
    def desapilar(pila):
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamaño -= 1
        return x
    def pila_vacia(pila):
        return pila.cima is None
    def en_cima(pila):
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None
    def Tamaño(pila):
        return pila.tamaño
    def barrido(pila):
        paux = Pila()
        while(not pila_vacia(pila)):
            dato = desapilar(pila)
            print(dato)
            apilar(paux, dato)
        while(not pila_vacia(paux)):
            dato = desapilar(paux)
            apilar(pila, dato)