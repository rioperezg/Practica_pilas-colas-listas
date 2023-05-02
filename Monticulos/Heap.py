class Heap(object):
    def __init__(self, tamaño):
        self.tamaño = 0
        self.vector = [None] * tamaño
    def intercambio(vector, indice1, indice2):
        aux = vector[indice1]
        vector[indice1] = vector[indice2]
        vector[indice2] = aux
    def flotar(heap, indice):
        while(indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]):
            padre = (indice - 1) // 2
            Heap.intercambio(heap.vector, indice, padre)
            indice = padre
    def hundir(heap, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while(control and hijo_izq < heap.tamaño):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < heap.tamaño):
                if(heap.vector[hijo_der] > heap.vector[hijo_izq]):
                    aux = hijo_der
            if(heap.vector[indice] < heap.vector[aux]):
                Heap.intercambio(heap.vector, indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False
    def agregar(heap, dato):
        heap.vector[heap.tamaño] = dato
        Heap.flotar(heap, heap.tamaño)
        heap.tamaño += 1
    def Quitar(heap):
        Heap.intercambio(heap.vector, 0, heap.tamaño - 1)
        dato = heap.vector[heap.tamaño - 1]
        heap.tamaño -= 1
        Heap.hundir(heap, 0)
        return dato
    def cantidad_elementos(heap):
        return heap.tamaño
    def heap_vacio(heap):
        return heap.tamaño == 0
    def heap_lleno(heap):
        return heap.tamaño == len(heap.vector)
    def monticulizar(heap):
        for i in range(len(heap.vector)):
            Heap.flotar(heap, i)
    # MONTICULO COMO COLA DE PRIORIDAD
    def arribo(heap, dato, prioridad):
        Heap.agregar(heap, [prioridad, dato])
    def atencion(heap):
        return Heap.Quitar(heap)[1]
    def cambiar_prioridad(heap, indice, prioridad):
        prioridad_anterior = heap[indice][0]
        heap[indice][0] = prioridad
        if(prioridad > prioridad_anterior):
            Heap.flotar(heap, indice)
        elif(prioridad < prioridad_anterior):
            Heap.hundir(heap, indice)