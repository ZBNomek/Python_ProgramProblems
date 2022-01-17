# 1. Si una vaca necesita M metros cuadrados de pasto para producir X litros de leche, ¿cu´antos
# litros de leche se producen en la granja?.
n: int = 6  # Corral de 6m^2
v: int = 5  # numero de vacas
vL: float = 2  # litos de leche por vaca
l: float  # litros de leche producida


def cantidad_de_leche(n, v, vL) -> float:
    leche: float = (n * v)/vL
    return leche


l = cantidad_de_leche(n, v, vL)
print(l)
