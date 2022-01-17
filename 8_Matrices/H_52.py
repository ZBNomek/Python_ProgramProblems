# 52. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

from H_50 import print_matriz


def lista_suma_columnas_matriz(matriz_A: list) -> list:
    temp: list = []
    n: int = 0
    for e in matriz_A[0]:
        h: list = []
        for i in matriz_A:
            h.append(i[n])
        temp.append(h)
        n += 1
    return temp


def suma_lista(lista: list):
    a: int = 0
    for i in lista:
        a += i
    return a


def suma_listas(lista: list):
    a: int
    temp: list = []
    for i in lista:
        a = suma_lista(i)
        temp.append(a)
    return temp


def suma_columnas_matriz(matriz_A: list) -> list:
    temp: list = lista_suma_columnas_matriz(matriz_A)
    temp = suma_listas(temp)
    return temp


"""
matriz_A: list = [[5, 3, -4], [8, -1, 0], [-7, 2, 1], [-2, -2, -1]]


print_matriz(matriz_A)
print("____________________")
suma: list = suma_columnas_matriz(matriz_A)
for x in range(len(suma)):
    print(suma[x], '  ', end=" ")
"""
