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
        if pila.cima is None:
           return None  # pila vacía
        x = pila.cima.info      # guardas el valor real
        pila.cima = pila.cima.sig  # mueves la cima al siguiente nodo
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
        while not Pila.pila_vacia(pila):
            dato = Pila.desapilar(pila)
            print(dato)
            Pila.apilar(paux, dato)

        while(Pila.pila_vacia(paux) != None):
            dato = Pila.desapilar(paux)
            Pila.apilar(pila, dato)