API = [101, 102, 103, 104, 105, 106]
WEB = [104, 105, 106, 107, 108]
ERRORES = [102, 105, 109]

#Usuarios que utilizan ambas plataformas.
contenedor_ambas = [0]* 5
cantidad_ambas = 0
for i in range(6):
    for j in range(5):
        if API[i] == WEB[j]:
            contenedor_ambas[cantidad_ambas] = API[i]
            cantidad_ambas += 1
vector_ambas = [0] * cantidad_ambas
for i in range (cantidad_ambas):
    vector_ambas[i]= contenedor_ambas[i]
print("Usuarios que utilizan ambas plataformas:", vector_ambas)

#Usuarios que utilizan al menos una plataformas.
contenedor = [0]*11
cantidad = 0
for i in range (6):
    contenedor[cantidad] = API[i]
    cantidad += 1
for i in range (5):
    existe = False
    for j in range(cantidad):
        if WEB[i] == contenedor[j]:
            existe = True
    if existe == False:
        contenedor[cantidad] = WEB[i]
        cantidad +=1
vector_final = [0] * cantidad
for i in range(cantidad):
    vector_final[i] = contenedor [i]
print("Usuarios que utilizan al menos una plataforma:", vector_final)

#Usuarios que utilizan la plataforma, pero no presentan errores.
contenedor_sin_errores = [0] * cantidad
cantidad_sin_errores = 0
for i in range(cantidad):
    tiene_error = False
    for j in range (3):
        if vector_final[i] == ERRORES[j]:
            tiene_error = True
    if tiene_error == False:
        contenedor_sin_errores[cantidad_sin_errores] = vector_final[i]
        cantidad_sin_errores += 1
vector_sin_errores = [0]* cantidad_sin_errores
for i in range (cantidad_sin_errores):
    vector_sin_errores[i] = contenedor_sin_errores [i]
print("Usuarios que utilizan la plataforma, pero no presentan errores:", vector_sin_errores)


#Tabla de verdad
def es_usruario_critico(p,q,r):
    resultado = (p or q) and r
    return resultado
combinaciones = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (True, False, False),
    (False, True, True),
    (False, True, False),
    (False, False, True),
    (False, False, False)
]
print("\np", "\tq", "\tr", "\tUsuario Crítico\n")

for p,q,r in combinaciones:
    salida = es_usruario_critico(p,q,r)
    print(p, "\t", q, "\t", r, "\t", salida)
