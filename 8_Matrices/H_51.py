# 51. Desarrollar un algoritmo que permita multiplicar dos matrices de n´umeros reales (enteros).
from H_50 import print_matriz


def posibilidad_de_multiplicacion(matriz_A: list, matriz_B: list) -> bool:
    flag: bool
    if len(matriz_A[0]) == len(matriz_B):
        flag = True
    else:
        flag = False
    return flag


def suma_elementos_lista(lista: list) -> int:
    n: int = 0
    for i in lista:
        n += i
    return n


def multiplicacion_de_matrices(matriz_A: list, matriz_B: list) -> list:
    flag: bool = posibilidad_de_multiplicacion(matriz_A, matriz_B)
    matriz_AxB: list = []
    if flag == True:
        l: int = 0
        for a in matriz_A:
            temp: list = []
            m: int = 0
            for e in matriz_B[0]:
                n: int = 0
                h: int = 0
                for i in matriz_A[l]:
                    h += i * matriz_B[n][m]
                    n += 1
                m += 1
                temp.append(h)
            l += 1
            matriz_AxB.append(temp)
    else:
        print("Las matrices dadas no pueden ser multiplicadas")

    return matriz_AxB


matriz_A: list = [[5, 3, -4, -2], [8, -1, 0, -3]]
matriz_B: list = [[1, 4, 0], [-5, 3, 7], [0, -9, 5], [5, 1, 4]]

a: list = multiplicacion_de_matrices(matriz_A, matriz_B)
print_matriz(a)
