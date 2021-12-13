# 25. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de n´umeros enteros
# (reales) de igual tama˜no. Sean v = (v1, v2, . . ., vn) y w = (w1, w2, . . ., wn) dos arreglos, el
# producto de v y w(notado v ⋅ w) es el n´umero: v1 ∗ w1 + v2 ∗ w2 + ⋯ + vn ∗ wn.

def producto_punto_elem(arreglo_1: list, arreglo_2: list) -> int:
    n: int = 0
    producto: int = 0
    for i in arreglo_1:
        i *= arreglo_2[n]
        producto += i
        n += 1
    return producto


"""
arreglo_1: list = [1, 2, 3, 5]
arreglo_2: list = [3, 6, 5, 12]

print(producto_punto_elem(arreglo_1, arreglo_2))
"""
