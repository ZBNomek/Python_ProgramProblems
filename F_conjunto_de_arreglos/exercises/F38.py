# 38. Diferencia sim´etrica: Calcula en un arreglo la diferencia sim´etrica de los conjuntos y la
# imprime.
from F37 import diferencia_conjuntos
from F35 import union_conjuntos


def diferencia_sim_conjuntos(a: list, b: list):
    temp: list = union_conjuntos(
        diferencia_conjuntos(a, b), diferencia_conjuntos(b, a))
    print(union_conjuntos(
        diferencia_conjuntos(a, b), diferencia_conjuntos(b, a)))
    return temp
