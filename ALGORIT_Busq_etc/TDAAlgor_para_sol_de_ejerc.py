from algorit_Busqueda_etc import dijkstra, Kruskal
from Herramientas_necesarias import Pila, Cola, Heap, Grafo, Arista
grafo = Grafo(False)
cargar_grafo(grafo)
Arista.barrido_profundo(grafo, grafo.inicio)
Arista.marcar_no_visitado(grafo)
Arista.barrido_amplitud(grafo, grafo.inicio)

origen = Arista.buscar_vertice(grafo, 'T')
destino = Arista.buscar_vertice(grafo, 'Z')
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(Arista.existe_paso(grafo, origen, destino)):
        camino_mas_corto = dijkstra(grafo, "T", "Z")
        fin = destino.info
        while(not Pila.pila_vacia(camino_mas_corto)):
            dato = Pila.desapilar(camino_mas_corto)
            if(fin == dato[1][0].info):
                print(dato[1][0].info)
                fin = dato[1][1]
Arista.marcar_no_visitado(grafo)
arbol_minimo = Kruskal(grafo)
print(arbol_minimo)