# 15. Dadas la pendiente y el punto de corte de dos rectas, determinar los puntos de intersecci´on al
# origen.

def interseccion_origen(valores_ecuacion: tuple) -> tuple:
    # ---> { valores_ecuacion[0] = pendiente | valores_ecuacion[1] = corte en y de la funcion }
    corte_x: float = -valores_ecuacion[1]/valores_ecuacion[0]
    # ---> Develve (x,y) = x siendo la abcisa al origen | y siendo la ordenada al origen
    return corte_x, valores_ecuacion[1]


"""
recta_1: tuple = (2, -1)
recta_2: tuple = (5, 3)

print(interseccion_origen(recta_1))
print(interseccion_origen(recta_2))
"""
