# 56. Desarrollar un programa que calcule el determinante de una matriz cuadrada.

from H_52 import suma_lista
from H_54 import lista_suma_diagonales_matriz_izq_der, lista_suma_diagonales_matriz_der_izq
from copy import deepcopy


def multiplicacion_elem_list(lista: list):
    x: int = 1
    for i in lista:
        x *= i
    return x


def crear_matriz_signos(matriz_A):
    matriz_signos = []
    flag = False
    n: int
    for i in matriz_A:
        temp = []
        if flag == False:
            n = 1
        elif flag == True:
            n = -1

        if n == 1:
            flag = True
        else:
            flag = False
        for i in matriz_A:
            temp.append(n)
            if n == 1:
                n = -1
            else:
                n = 1
        matriz_signos.append(temp)
    return matriz_signos


def determinante_2x2(matriz_A):
    a: int = multiplicacion_elem_list(
        lista_suma_diagonales_matriz_izq_der(matriz_A))
    b: int = multiplicacion_elem_list(
        lista_suma_diagonales_matriz_der_izq(matriz_A))
    return a - b


def adjuntos_lapace(signos, matriz_A, n):
    b: int = matriz_A[-1][n]
    signo: int = signos[-1][n]

    copia_matriz: list = deepcopy(matriz_A)

    del copia_matriz[-1]

    for i in copia_matriz:
        del i[n]

    signo *= determinante_2x2(copia_matriz)
    b *= signo

    return b


def determinante_Lapace(matriz_A):
    n = 0
    signos = crear_matriz_signos(matriz_A)
    temp_list: list = []

    for i in matriz_A[-1]:
        adj = adjuntos_lapace(signos, matriz_A, n)
        temp_list.append(adj)
        n += 1

    temp_list = suma_lista(temp_list)
    return temp_list


def matriz_cuadrada(matriz_A):
    flag: bool
    if len(matriz_A) == len(matriz_A[-1]):
        flag = True
    else:
        flag = False

    return flag


def determinante_matriz(matriz_A):
    flag: bool = matriz_cuadrada(matriz_A)
    if flag == True:
        flag = False
        determinante: int
        if len(matriz_A) == 2:
            determinante = determinante_2x2(matriz_A)
        elif len(matriz_A) == 3:
            determinante = determinante_Lapace(matriz_A)
        else:
            flag = True
            print("""
            Creo que ya probe que puedo hacer operaciones con matrices,
            y que domino el python en este tema. Ahora, el tema de
            matrices no mucho. En conclución:
            
            >>> Error, matriz muy grande para el programa
            """)

        if flag:
            return TypeError
        else:
            return determinante

    else:
        print("No es una matriz cuadrada!!!")
        return TypeError


"""
matriz_A: list = [[5, -3], [6, 4]] #matriz 2x2
#matriz_A: list = [[10, -2, 0], [5, -4, 7], [3, 1, -1]] #matriz 3x3
#matriz_A = [[1, -2, -1, 3], [-1, 3, -2, -2], [2, 0, 1, 1], [1, -2, 2, 3]]#matriz 4x4 (no valida en este programa)

#matriz_A: list = [[10, -2, 0], [5, -4, 7], [3, 1, -1], [3, 6, 4]]#matriz no cuadrada

print(determinante_matriz(matriz_A))
"""
