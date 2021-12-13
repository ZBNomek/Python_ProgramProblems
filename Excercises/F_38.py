# 38. Diferencia sim´etrica: Calcula en un arreglo la diferencia sim´etrica de los conjuntos y la
# imprime.
from F_37 import diferencia_conjuntos
from F_35 import union_conjuntos


def diferencia_sim_conjuntos(conjunto_a: list, conjunto_b: list) -> list:
    lista_diferencia_sim: list = union_conjuntos(
        diferencia_conjuntos(conjunto_a, conjunto_b), diferencia_conjuntos(conjunto_b, conjunto_a))
    return lista_diferencia_sim


"""
conjunto_a: list = [1, 3, 5, 7, 9]
conjunto_b: list = [5, 6, 7, 9, 11, 15]

print(diferencia_sim_conjuntos(conjunto_a, conjunto_b))
"""
