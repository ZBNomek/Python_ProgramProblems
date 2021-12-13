# 29. Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La
# mediana es el n´umero que queda en la mitad del arreglo despu´es de ser ordenado.

from B_08 import ordenar_valores


def mediana_elem(arreglo: list) -> float:
    arreglo = ordenar_valores(arreglo)
    lenght: int = len(arreglo)
    if lenght % 2 == 0:
        mediana: float = (arreglo[int(lenght/2)] +
                          arreglo[int((lenght/2)-1)])/2
    else:
        mediana: int = arreglo[int((lenght-1)/2)]
    return mediana


"""
arreglo_par: list = [2, 7, 4, 1, 3]
print("Mediana = ", mediana_elem(arreglo_par))
arreglo_impar: list = [2, 7, 4, 1, 3, 6]
print("Mediana = ", mediana_elem(arreglo_impar))
"""
