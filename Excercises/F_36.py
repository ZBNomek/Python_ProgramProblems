# 36. Intersecci´on: Calcula en un arreglo la intersecci´on de los conjuntos y la imprime.

def interseccion_conjuntos(conjunto_a: list, conjunto_b: list) -> list:
    lista_interseccion: list = []
    for i in conjunto_a:
        if i in conjunto_b:
            lista_interseccion.append(i)
    return lista_interseccion


"""
conjunto_a: list = [1, 3, 5, 7, 9]
conjunto_b: list = [5, 6, 7, 9, 11, 15]

print(interseccion_conjuntos(conjunto_a, conjunto_b))
"""
