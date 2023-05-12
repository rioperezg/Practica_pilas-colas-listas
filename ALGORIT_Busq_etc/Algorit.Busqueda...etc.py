from Herramientas_necesarias import Heap, Pila, Arista, inf
def dijkstra(grafo, origen, destino):
    no_visitados = Heap(Pila.Tamaño(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            Heap.arrib_H(no_visitados, [aux, None], 0)
        else:
            Heap.arrib_H(no_visitados, [aux, None], inf)
        aux = aux.sig
    while(not Heap.heap_vacio(no_visitados)):
        dato = Heap.atencion_H(no_visitados)
        Pila.apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_H(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0]>dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                Heap.cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino

def prim(grafo):
    bosque = [[grafo.inicio.info]]
    aristas = []
    adyacentes = grafo.inicio.adyacentes.inicio
    while(adyacentes is not None):
        aristas.append([grafo.inicio.info, adyacentes.destino, adyacentes.info])
        adyacentes = adyacentes.sig
    while(len(bosque[0]) // 2 < Pila.Tamaño(grafo) - 1):
        menor = inf
        menor_arista = None
        tipo = None
        for arista in aristas:
            origen = arista[0]
            destino = arista[1]
            if(origen not in bosque[0] and destino in bosque[0]):
                if(arista[2] < menor):
                    menor, menor_arista = arista[2], arista
                    tipo = True
            if(origen in bosque[0] and destino not in bosque[0]):
                if(arista[2] < menor):
                    menor, menor_arista = arista[2], arista
                    tipo = False

        arista = aristas.pop(aristas.index(menor_arista))
        if(len(bosque[0] != 1)):
            bosque[0] += [arista[0], arista[1]]
        else:
            bosque.pop()
            bosque.append([arista[0], arista[1]])
        aux = None
        if(tipo):
            aux = Arista.buscar_vertice(grafo, arista[0])
        else:
            aux = Arista.buscar_vertice(grafo, arista[1])
        adyacentes = aux.adyacentes.inicio
        while(adyacentes is not None):
            aristas.append([aux.info, adyacentes.destino, adyacentes.info])
            adyacentes = adyacentes.sig
    return bosque
def Kruskal(grafo):
    bosque = []
    aristas = Heap(Pila.Tamaño(grafo) ** 2)
    aux = grafo.inicio
    while(aux is not None):
        bosque.append([aux.info])
        adyacentes = aux.adyacentes.inicio
        while(adyacentes is not None):
            Heap.arrib_H(aristas, [aux.info, adyacentes.destino], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig
    while(len(bosque) > 1 and not Heap.heap_vacio(aristas)):
        dato = Heap.atencion_H(aristas)
        origen = None
        for elemento in bosque:
            if(dato[1][0] in elemento):
                origen = bosque.pop(bosque.index(elemento))
        destino = None
        for elemento in bosque:
            if(dato[1][1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
        if(origen is not None and destino is not None):
            if(len(origen) > 1 and len(destino) == 1):
                destino.insert(0, dato[1][0])
            elif(len(destino) > 1 and len(origen) == 1):
                origen.append(dato[1][1])
            elif(len(destino) > 1 and len(origen) > 1):
                origen += [dato[1][0], dato[1][1]]
            bosque.append(origen + destino)	
        else:
            bosque.append(origen)
    return bosque