# 31. Suponga que un arreglo de enteros esta lleno de unos y ceros y que el arreglo representa un
# n´umero binario al rev´es. Hacer un algoritmo que calcule los n´umeros en decimal que representa
# dicho arreglo de unos y ceros.

from E_23 import suma_elem
from E_28 import producto_directo_elem


def binario_a_decimal(numero_binario: list):
    n = 0
    multiplicadores = []
    for i in numero_binario:
        multiplicadores.append(pow(2, n))
        n += 1

    numero_decimal = suma_elem(
        producto_directo_elem(numero_binario, multiplicadores))
    return numero_decimal


"""
binario_1: list = [0, 1, 0, 1, 0, 1, 1]  # 106
binario_2: list = [1, 0, 0, 1, 0, 1, 1, 1, 1]  # 489

print("[0, 1, 0, 1, 0, 1, 1] = ",binario_a_decimal(binario_1))
print("[1, 0, 0, 1, 0, 1, 1, 1, 1] = ",binario_a_decimal(binario_2))
"""
