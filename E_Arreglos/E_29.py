# 29. Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La
# mediana es el n´umero que queda en la mitad del arreglo despu´es de ser ordenado.


arreglo: list = [2, 7, 4, 1, 3]


def ordenar_elem(arreglo):
    arreglo_ordenado: list = [None]*len(arreglo)
    for i in arreglo:
        t = 0
        for e in arreglo:
            if i <= e:
                t += 1
            else:
                pass
        arreglo_ordenado[-t] = i
    return arreglo_ordenado


def mediana_elem(arreglo: list):
    arreglo = ordenar_elem(arreglo)
    print("Arreglo ordenado = ", arreglo)
    lenght: int = len(arreglo)
    if lenght % 2 == 0:
        mediana: float = (arreglo[int(lenght/2)] +
                          arreglo[int((lenght/2)-1)])/2
    else:
        mediana: int = arreglo[int((lenght-1)/2)]
    return mediana


print("Mediana = ", mediana_elem(arreglo))
