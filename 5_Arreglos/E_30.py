# 30. Hacer un algoritmo que deje al final de un arreglo de n´umeros todos los ceros que aparezcan
# en dicho arreglo.

def ordenar_ceros(arreglo: list) -> list:
    list_temp: list = [*arreglo]
    t = 0
    for i in list_temp:
        if i == 0:
            arreglo.remove(i)
            t += 1
        else:
            pass
    arreglo += [0]*t
    return arreglo


"""
arreglo: list = [2, 5, 0, 5, 0, 3, 0, 0, 1]
print(ordenar_ceros(arreglo))
"""
