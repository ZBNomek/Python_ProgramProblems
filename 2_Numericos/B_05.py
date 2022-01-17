# 5. Función potencia de un entero elevado a un entero.

# Esto se puede hacer con la funcion pow()



def potencia(base: int, exponente: float) -> float:
    negativo: bool = False
    potencia: float = 1
    if exponente < 0:
        negativo = True
        exponente *= -1
    while exponente > 0:
        potencia *= base
        exponente -= 1
    if negativo == True:
        potencia = 1/potencia
    return potencia

"""
base = 5
exponente = 2
print(potencia(base, exponente))
"""