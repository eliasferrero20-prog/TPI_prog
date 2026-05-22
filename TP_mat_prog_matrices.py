M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]
C = [
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
]
for i in range(3):
    suma_fila = 0
    for j in range(3):
        suma_fila = suma_fila + M[i][j]
    promedio_f = suma_fila / 3
    print("Tiempo promedio de ejecución - Función", i + 1, ":", promedio_f, "ms")
for j in range(3):
    suma_columna = 0
    for i in range(3):
        suma_columna = suma_columna + M[i][j]
    promedio_s = suma_columna / 3
    print("Tiempo promedio de ejecución - Servidor", j + 1, ":", promedio_s, "ms")

MT = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(3):
    for j in range(3):
        MT[j][i] = M[i][j]

print("Matriz Transpuesta:")
for fila in MT:
    print(fila)