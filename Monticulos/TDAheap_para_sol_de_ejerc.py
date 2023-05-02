from Heap import Heap
from random import randint

heap = Heap(10)

while(not Heap.heap_lleno(heap)):
    num = randint(0, 500)
    prioridad = randint(1, 3)
    Heap.agregar(heap, [prioridad, num])
print(heap.vector)
while not Heap.heap_vacio(heap):
    dato = Heap.atencion(heap)
    print(dato)