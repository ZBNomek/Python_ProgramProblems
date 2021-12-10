# 26. Desarrollar un algoritmo que calcule el m´ınimo de un arreglo de n´umeros enteros(reales).

arreglo: list = [7, 10, 90, 5, 15, 84]


def min_elem(arreglo: list):
    n_min: int = arreglo[0]
    for i in arreglo:
        if i < n_min:
            n_min = i
        else:
            pass
    return n_min


# print(min_elem(arreglo))
