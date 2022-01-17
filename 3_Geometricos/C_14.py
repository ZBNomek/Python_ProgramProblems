# 14. Dadas la pendiente y el punto de corte de dos rectas, determinar si son paralelas, perpendiculares o ninguna de las anteriores.

# Ecuacion lienar = { m = pendiente | b = punto de corte con el eje y}

def tipo_de_recta(pendiente_recta_1: float, corte_y_recta_1: float, pendiente_recta_2: float, corte_y_recta_2: float) -> str:
    tipo: str
    y: float
    if pendiente_recta_1 == pendiente_recta_2:
        if corte_y_recta_1 == corte_y_recta_2:
            tipo = "iguales"
        else:
            tipo = "paralelas"
    else:
        y = -1/(pendiente_recta_1)
        if y == pendiente_recta_2:
            tipo = ("perpendicular")
        else:
            tipo = ("ninguno")
    return tipo


"""
recta_1: tuple = (2, -1)  # ---> y = 2x - 1
recta_2: tuple

# iguales
recta_2 = (2, -1)  # ---> y = 2x - 1
print(tipo_de_recta(recta_1[0], recta_1[1], recta_2[0], recta_2[1]))

# paralelas
recta_2 = (2, 1)  # ---> y = 2x + 1
print(tipo_de_recta(recta_1[0], recta_1[1], recta_2[0], recta_2[1]))

# perpendiculares
recta_2 = (-0.5, -1)  # ---> y = -1/2x - 1
print(tipo_de_recta(recta_1[0], recta_1[1], recta_2[0], recta_2[1]))

recta_2 = (3, -1)  # ---> y = 3x - 1
print(tipo_de_recta(recta_1[0], recta_1[1], recta_2[0], recta_2[1]))
"""
