# 54. Desarrollar un algoritmo que determine si una matriz es m´agica. Se dice que una matriz
# cuadrada es m´agica si la suma de cada una de sus filas, de cada una de sus columnas y de
# cada diagonal es igual.
from H_50 import print_matriz
from H_52 import suma_columnas_matriz, suma_listas, suma_lista
from H_53 import suma_filas_matriz


def lista_suma_diagonales_matriz_izq_der(matriz):
    temp: list = []
    n = 0
    for i in matriz:
        temp.append(i[n])
        n += 1
    return temp


def suma_diagonales_matriz_izq_der(temp: list):
    temp = lista_suma_diagonales_matriz_izq_der(temp)
    temp = [suma_lista(temp)]
    return temp


def lista_suma_diagonales_matriz_der_izq(matriz):
    temp: list = []
    n = -1
    for i in matriz:
        temp.append(i[n])
        n -= 1
    return temp


def suma_diagonales_matriz_der_izq(temp: list):
    temp = lista_suma_diagonales_matriz_der_izq(temp)
    temp = [suma_lista(temp)]
    return temp


def flag_verification(suma: list):
    flag: bool = False
    n: int = 0
    a: int = suma[n]
    for i in suma:
        try:
            if a == suma[n+1]:
                flag = True
            n += 1
        except:
            IndexError
    return flag


def matriz_magica(matriz_A):
    flag: bool
    suma: list
    x: int
    y: int

    suma = suma_filas_matriz(matriz_A)
    x = suma[0]
    flag = flag_verification(suma)
    if flag == True:
        flag = False
        suma = suma_columnas_matriz(matriz_A)
        y = suma[0]
        flag = flag_verification(suma)
    if flag == True:
        flag = False
        if x == y:
            flag = True
    if flag == True:
        flag = False
        suma = suma_diagonales_matriz_izq_der(matriz_A)
        if (suma[0] == y) or (suma[0] == x):
            flag = True
    if flag == True:
        flag = False
        suma = suma_diagonales_matriz_der_izq(matriz_A)
        if (suma[0] == y) or (suma[0] == x):
            flag = True

    return flag


"""

matriz_A = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
#matriz_A = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print()
print_matriz(matriz_A)
print()
print("Matriz Mágica =", matriz_magica(matriz_A))
print()
"""
