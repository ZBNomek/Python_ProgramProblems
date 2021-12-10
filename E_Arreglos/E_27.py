# 27. Desarrollar un algoritmo que calcule el m´aximo de un arreglo de n´umeros enteros (reales).

arreglo: list = [7, 10, 90, 5, 15, 84]


def max_elem(arreglo: list):
    n_max: int = arreglo[0]
    for i in arreglo:
        if i > n_max:
            n_max = i
        else:
            pass
    return n_max


# print(max_elem(arreglo))
