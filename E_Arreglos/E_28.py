# 28. Desarrollar un algoritmo que calcule el producto directo de dos arreglos de enteros (reales) de
# igual tama˜no. Sean v = (v1, v2, . . . , vn) y w = (w1, w2, . . . , wn) dos arreglos, el producto directo
# de v y w (notado v ∗ w) es el vector: (v1 ∗ w1, v2 ∗ w2, . . . , vn ∗ wn).


arreglo_1: list = [1, 8, 34, 7]
arreglo_2: list = [6, 23, 4, 79]


def producto_directo_elem(arreglo_1: list, arreglo_2: list):
    producto: list = []
    n = 0
    for i in arreglo_1:
        i *= arreglo_2[n]
        producto.append(i)
        n += 1
    return producto


#print(producto_directo_elem(arreglo_1, arreglo_2))
