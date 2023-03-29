from Tablas import crear_tabla, agregar1, buscar2
tabla = crear_tabla(9)
nombre = input("Ingrese nombre")
while(nombre != ""):
    agregar1(tabla, nombre)
    nombre = input("Ingrese nombre")
buscado = input("Ingrese el nombre a buscar")
posicion = buscar2(tabla, buscado)
if(posicion is not None):
    print("Elemento encontrado", posicion.info)
else:
    print("No se encontro el elemento buscado")
    