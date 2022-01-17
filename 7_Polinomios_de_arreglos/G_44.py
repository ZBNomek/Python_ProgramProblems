# 44. Sumar: Calcula el polinomio suma y lo imprime.

def igualar_polinomios(polinomio_1: list, polinomio_2: list) -> list:
    lenght: list
    turn_flag: bool = False
    if len(polinomio_1) > len(polinomio_2):
        lenght = len(polinomio_1) - len(polinomio_2)
    elif len(polinomio_1) < len(polinomio_2):
        polinomio_1, polinomio_2 = polinomio_2, polinomio_1
        lenght = len(polinomio_1) - len(polinomio_2)
        turn_flag = True
    else:
        lenght = 0
    while lenght > 0:
        polinomio_2.insert(0, 0)
        lenght -= 1
    if turn_flag == True:
        polinomio_1, polinomio_2 = polinomio_2, polinomio_1
    return polinomio_1, polinomio_2


def suma_polinomios(polinomio_1: list, polinomio_2: list) -> list:
    polinomios_igualados: list = igualar_polinomios(polinomio_1, polinomio_2)
    suma: list = []
    index: int = 0
    for i in polinomios_igualados[0]:
        suma.append(i+polinomios_igualados[1][index])
        index += 1
    return suma


"""
polinomio_1 = [2, 1, -3]  # 2x^2 + x - 3
polinomio_2 = [1, -3, 1]  # x^2 - 3x + 1
# 2x^ + x - 3 + x^2 - 3x + 1 = 3x^2 - 2x - 2

print(suma_polinomios(polinomio_1, polinomio_2))

# polinomio_1 = [2, 1, -3]  # 2x^2 + x - 3
polinomio_3 = [2, -5]  # 2x - 5
# 2x^2 + x - 3 + 0x^2 +2x - 5 = 2x^2 + 3x - 8

print(suma_polinomios(polinomio_1, polinomio_3))
"""
