# 45. Resta: Calcula el polinomio resta y lo imprime.

from G_44 import igualar_polinomios


def resta_polinomios(polinomio_1: list, polinomio_2: list) -> list:
    polinomios_igualados: list = igualar_polinomios(polinomio_1, polinomio_2)
    resta: list = []
    index: int = 0
    for i in polinomios_igualados[0]:
        resta.append(i-polinomios_igualados[1][index])
        index += 1
    return resta


"""
polinomio_1 = [2, 1, -3]  # 2x^2 + x - 3
polinomio_2 = [1, -3, 1]  # x^2 - 3x + 1
# 2x^ + x - 3 - (x^2 - 3x + 1) = x^2 + 4x - 4

print(resta_polinomios(polinomio_1, polinomio_2))

# polinomio_1 = [2, 1, -3]  # 2x^2 + x - 3
polinomio_3 = [2, -5]  # 2x - 5
# 2x^2 + x - 3 + 0x^2 +2x - 5 = 2x^2 + 3x - 8

print(resta_polinomios(polinomio_1, polinomio_3))
"""
