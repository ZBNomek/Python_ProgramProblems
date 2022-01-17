# 9. Determinar si un n´umero es m´ultiplo de la suma de otros dos n´umeros.

def multiplo_de_una_suma(multiplo: int, numero_1: int, numero_2: int) -> bool:
    multiplo_bool = False
    if multiplo > (numero_1 + numero_2):
        if multiplo % (numero_1 + numero_2) == 0:
            multiplo_bool = True
    return multiplo_bool


"""
print(multiplo_de_una_suma(25, 2, 3))  # --->True
print(multiplo_de_una_suma(20, 4, 3))  # --->False
"""
