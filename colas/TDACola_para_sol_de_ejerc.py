from colas import colas

cdatos = colas.Cola()
cvocales = colas.Cola()

letra = input("Ingrese un caracter")
while(letra != ""):
    colas.Cola.arribo(cdatos, letra)
    letra = input("ingrese un caracter")
while(not colas.Cola.cola_vacia(cdatos)):
    letra = colas.Cola.atencion(cdatos)
    if letra.upper() in ["A", "E", "i", "o", "u"]:
        colas.Cola.arribo(cvocales, letra)
print("Datos cola vocales")
while(not colas.Cola.cola_vacia(cvocales)):
    dato = colas.Cola.atencion(cvocales)
    print(dato)