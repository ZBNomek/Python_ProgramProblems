# 23. Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de n´umeros enteros
# (reales).

def suma_elem(arreglo: list) -> int:
    a: int = 0

    for i in arreglo:
        a += i
    return a


"""
arreglo: list = [1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 30]
print(suma_elem(arreglo))
"""
