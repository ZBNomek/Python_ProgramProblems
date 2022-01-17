# 50. Desarrollar un algoritmo que permita sumar dos matrices de n´umeros reales (enteros).

def mismo_tamaño_matrizes(matriz_A: list, matriz_B: list) -> bool:
    flag = False
    if len(matriz_A) == len(matriz_B):
        if len(matriz_A[0]) == len(matriz_B[0]):
            flag = True

    return flag


def suma_matrices(matriz_A: list, matriz_B: list) -> list:
    flag = mismo_tamaño_matrizes(matriz_A, matriz_B)
    matriz_A_plus_B: list = []
    if flag == True:
        n: int = 0
        temp: list

        for i in matriz_A:
            temp = []
            for e in i:
                temp.append(matriz_A[n][matriz_A[n].index(e)] +
                            matriz_B[n][matriz_A[n].index(e)])
            n += 1
            matriz_A_plus_B.append(temp)
    else:
        print("Las matrices dadas no son del miso tamaño por lo que no se pueden sumar")

    return matriz_A_plus_B


def print_matriz(matriz: list) -> None:
    print('\n'.join(['\t'.join([str(cell) for cell in row])
          for row in matriz]))


"""
matriz_A: list = [[2, 3, 4], [1, 2, 5]]
matriz_B: list = [[7, 1, 4], [0, 8, 2]]
#matriz_A = [[2, 3, 4], [1, 2, 5], [6, 3, 1]]

print_matriz(suma_matrices(matriz_A, matriz_B))
"""
