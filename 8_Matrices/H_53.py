# 53. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
from H_50 import print_matriz
from H_52 import suma_listas


matriz_A: list = [[5, 3, -4], [8, -1, 0], [-7, 2, 1], [-2, -2, -1]]


def lista_suma_filas_matriz(matriz_A: list) -> list:
    temp: list = []
    h: list
    for e in matriz_A:
        h = []
        for i in e:
            h.append(i)
        temp.append(h)
    return temp


def suma_filas_matriz(matriz_A):
    temp: list = lista_suma_filas_matriz(matriz_A)
    temp = suma_listas(temp)
    return temp


"""
print_matriz(matriz_A)
print("_____________________")
suma: list = suma_filas_matriz(matriz_A)
for x in range(len(suma)):
    print(suma[x], "  ", end=" ")
"""
