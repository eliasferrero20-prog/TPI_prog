#Tabla de verdad.
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
print("p", "\tq", "\tr", "\tUsuario Crítico\n")
for p,q,r in combinaciones:
    salida = es_usruario_critico(p,q,r)
    print(p, "\t", q, "\t", r, "\t", salida)
