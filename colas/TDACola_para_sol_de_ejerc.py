from colas import Cola

cdatos = Cola()
cvocales = Cola()

letra = input("Ingrese un caracter")
while(letra != ""):
    Cola.arribo(cdatos, letra)
    letra = input("ingrese un caracter")
while(not Cola.cola_vacia(cdatos)):
    Cola.atencion(cdatos, letra)
    if letra.upper() in ["A", "E", "i", "o", "u"]:
        Cola.arribo(cvocales, letra)
print("Datos cola vocales")
print(Cola.barrido(cvocales))
while(not Cola.cola_vacia(cvocales)):
    dato = Cola.atencion(cvocales)
    print(dato)