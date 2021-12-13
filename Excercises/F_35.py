# 35. Uni´on: Calcula en un arreglo la uni´on de los conjuntos y la imprime

from B_08 import ordenar_valores


def union_conjuntos(conjunto_a: list, conjunto_b: list) -> list:
    lista_union: list = []
    for i in conjunto_a:
        lista_union.append(i)
    for i in conjunto_b:
        if i not in conjunto_a:
            lista_union.append(i)
    return ordenar_valores(lista_union)


"""
conjunto_1: list = [8, 1, 5, 6, 14, 5, 52]
conjunto_2: list = [1, 2, 3, 4, 5]

print(union_conjuntos(conjunto_1, conjunto_2))
"""
