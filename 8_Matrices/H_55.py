# 55. Desarrollar un algoritmo que dado un entero, reemplace en una matriz todos los n´umeros
# mayores a un n´umero dado por un uno y todos los menores o iguales por un cero.

from H_50 import print_matriz


def matriz_num_binario(matriz_A: list, n: int) -> list:
    ii: int = 0
    ei: int = 0
    for i in matriz_A:
        ei = 0
        for e in i:
            if e > n:
                matriz_A[ii][ei] = 1

            else:
                matriz_A[ii][ei] = 0
            ei += 1
        ii += 1

    return matriz_A


matriz_A: list = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
n: int = 5
print()
print_matriz(matriz_A)
print()
print_matriz(matriz_num_binario(matriz_A, n))
print()
