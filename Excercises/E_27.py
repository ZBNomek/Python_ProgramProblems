# 27. Desarrollar un algoritmo que calcule el m´aximo de un arreglo de n´umeros enteros (reales).

def max_elem(arreglo: list) -> int:
    elemento_max: int = arreglo[0]
    for i in arreglo:
        if i > elemento_max:
            elemento_max = i
    return elemento_max


"""
arreglo: list = [7, 10, 90, 5, 15, 84]
print(max_elem(arreglo))
"""
