"""
Una base espacial administra el despegue de sus naves utilizando una pila para organizar
los lanzamientos. Cada vez que una nave est´a lista para despegar, se apila su nombre en una estructura tipo
Pila. Sin embargo, por protocolo de seguridad, las naves deben despegar en orden inverso al de llegada.
Simula este comportamiento utilizando una pila. Muestra el orden de despegue y, al finalizar, comprueba
que la pila queda vac´ıa
"""
from pila import nodoPila, Pila
Naves = []
naves_pila = Pila()
for nave in Naves:
    Pila.apilar(naves_pila, nave)
n = Pila.Tamaño(naves_pila)
while n =! 0:
    Pila.desapilar(naves_pila)
    n -= 1