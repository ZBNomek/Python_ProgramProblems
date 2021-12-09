# 37. Diferencia: Calcula en un arreglo la diferencia del primero con el segundo y la imprime.

def diferencia_conjuntos(a: list, b: list):
    temp: list = []
    for i in a:
        if i not in b:
            temp.append(i)
        else:
            pass
    return temp
