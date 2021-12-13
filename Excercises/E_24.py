# 24. Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).

from E_23 import suma_elem


def promedio_elem(arreglo: list) -> float:
    promedio = suma_elem(arreglo)/len(arreglo)
    return promedio


"""
arreglo: list = [1, 2, 3, 4, 5, 10, 20, 40]
print(promedio_elem(arreglo))
"""
