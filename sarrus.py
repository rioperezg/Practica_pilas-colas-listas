class Matriz:
    def __init__(self, datos):
        self.datos = datos
        self.filas = len(datos)
        self.columnas = len(datos[0]) if datos else 0
    def obtener_elementos(self, fila, columna):
        return self.datos[fila][columna]
    def obtener_fila(self, fila):
        return self.datos[fila]
    def obtener_columna(self, columna):
        return [self.datos[fila][columna] for fila in range(self.filas)]
class Determinante:
    @staticmethod
    def calcular_recursiva(matriz):
        if matriz.filas != matriz.columnas:
            raise ValueError("La matriz debe ser cuadrada")
        if matriz.filas == 2:
            return matriz.obtener_elementos(0, 0) - matriz.obtener_elementos(1, 1) - matriz.obtener_elementos(0, 1) * matriz.obtener_elementos(1, 0)
        else:
            determinante = 0
            for col in range(matriz.columnas):
                submatriz_datos = [matriz.obtener_fila(fila)[0:col] + matriz.obtener_fila(fila)[col + 1:] for fila in range(1, matriz.filas)]
                submatriz = Matriz(submatriz_datos)
                determinante += (-1) ** col * matriz.obtener_elementos(0, col) * Determinante.calcular_recursiva(submatriz)
            return determinante