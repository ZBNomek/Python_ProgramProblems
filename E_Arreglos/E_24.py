from E_23 import suma_elem

arreglo: list = [1, 2, 3, 4, 5, 10, 20, 40]


def promedio_elem(arreglo: list):
    promedio = suma_elem(arreglo)/len(arreglo)
    return promedio


# print(promedio_elem(arreglo))
