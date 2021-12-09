# 35. Uni´on: Calcula en un arreglo la uni´on de los conjuntos y la imprime

def union_conjuntos(a: list, b: list):
    temp: list = []
    for i in a:
        temp.append(i)
    for i in b:
        if i not in a:
            temp.append(i)
    return temp
