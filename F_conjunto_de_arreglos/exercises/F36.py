# 36. Intersecci´on: Calcula en un arreglo la intersecci´on de los conjuntos y la imprime.

def interseccion_conjuntos(a: list, b: list):
    temp: list = []
    for i in a:
        if i in b:
            temp.append(i)
        else:
            pass
    return temp
