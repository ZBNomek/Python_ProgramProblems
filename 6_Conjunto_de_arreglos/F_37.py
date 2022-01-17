# 37. Diferencia: Calcula en un arreglo la diferencia del primero con el segundo y la imprime.

# ---> conjunto_a - conjunto_b
def diferencia_conjuntos(conjunto_a: list, conjunto_b: list) -> list:
    lista_diferencia: list = []
    for i in conjunto_a:
        if i not in conjunto_b:
            lista_diferencia.append(i)
    return lista_diferencia


"""
conjunto_a: list = [1, 3, 5, 7, 9]
conjunto_b: list = [5, 6, 7, 9, 11, 15]

# conjunto_a - conjunto_b
print(diferencia_conjuntos(conjunto_a, conjunto_b))

# conjunto_b - conjunto_a
print(diferencia_conjuntos(conjunto_b, conjunto_a))
"""
