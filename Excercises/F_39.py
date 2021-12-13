# 39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los
# conjuntos y lo imprime.

def pertenencia(n: int, conjunto_a: list, conjunto_b: list) -> list:
    flag_a: bool = False
    flag_b: bool = False

    for i in conjunto_a:
        if n == i:
            flag_a = True
            break
    for i in conjunto_b:
        if n == i:
            flag_b = True
            break
    lista_pertenecia: list = [flag_a, flag_b]
    return lista_pertenecia


"""
conjunto_a: list = [1, 3, 5, 7, 9]
conjunto_b: list = [5, 6, 7, 9, 11, 15]

# pertenece a conjunto_a y conjunto_b
print(pertenencia(5, conjunto_a, conjunto_b))

# pertenece a conjunto_a, no conjunto_b
print(pertenencia(1, conjunto_a, conjunto_b))

# pertenece a conjunto_b, no conjunto_a
print(pertenencia(11, conjunto_a, conjunto_b))

# no pertenece a ninguno
print(pertenencia(4, conjunto_a, conjunto_b))
"""
