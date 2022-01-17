# 26. Desarrollar un algoritmo que calcule el m´ınimo de un arreglo de n´umeros enteros(reales).

def min_elem(arreglo: list) -> int:
    elemento_min: int = arreglo[0]
    for i in arreglo:
        if i < elemento_min:
            elemento_min = i
    return elemento_min


"""
arreglo: list = [7, 10, 90, 5, 15, 84]
print(min_elem(arreglo))
"""
