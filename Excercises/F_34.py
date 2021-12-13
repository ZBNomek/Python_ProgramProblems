# 34. Hacer un algoritmo que calcule el M´ınimo Com´un M´ultiplo (MCM) para un arreglo de enteros
# positivos.

from B_08 import factorizacion
from E_27 import max_elem
from E_33 import cantidad_primos_en_conjunto, primos_a_decimal


def min_comun_multiplo(conjunto: list) -> int:
    lista_factorizacion_numeros = []
    valores_maximos = []
    for i in conjunto:
        lista_factorizacion_numeros.append(factorizacion(i))
        valores_maximos.append(max_elem(lista_factorizacion_numeros[-1]))

    max_val = max_elem(valores_maximos)
    valores_maximos = []  # -> vacio la lista para reusarla pero la dejo con el mismo nombre

    for factorizacion_numero in lista_factorizacion_numeros:
        valores_maximos.append(cantidad_primos_en_conjunto(
            factorizacion_numero, max_val))

    # -> reasigno los valore sde esta lista para reutilizarla pero no le cambio el nobre
    lista_factorizacion_numeros = [0, 0, 0]

    for i in valores_maximos:
        index = 0
        for n in i:
            lista_factorizacion_numeros[index] = max_elem(
                [lista_factorizacion_numeros[index], n])
            index += 1
    mcm = primos_a_decimal(lista_factorizacion_numeros)
    return mcm


"""
arreglo = [12, 20, 30, 15]
print(min_comun_multiplo(arreglo))
"""
