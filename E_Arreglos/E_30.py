# 30. Hacer un algoritmo que deje al final de un arreglo de n´umeros todos los ceros que aparezcan
# en dicho arreglo.

arreglo: list = [2, 5, 0, 5, 0, 3, 0, 0, 1]


def ordenar_ceros(arreglo: list):
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


print(ordenar_ceros(arreglo))
