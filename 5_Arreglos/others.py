"""
No pude hacer packetes para importar estas cosas de actividades anteriores
que se encuentran en carpetas disctintas por lo que la copio acá mientas
aprendo el como hacerlo
"""


def ordenar_valores(arreglo: list) -> list:
    arreglo_ordenado: list = [0]*len(arreglo)
    for i in arreglo:
        t: int = 0
        for e in arreglo:
            if i <= e:
                t += 1
            else:
                pass
        arreglo_ordenado[-t] = i
    for i in arreglo_ordenado:
        if i == 0:
            arreglo_ordenado[arreglo_ordenado.index(
                i)] = arreglo_ordenado[arreglo_ordenado.index(
                    i)-1]
    return arreglo_ordenado
