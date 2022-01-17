# 77. Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de
# caracteres. El corrimiento circular a izquierda es pasar el primer car´acter de una cadena como
# ´ultimo car´acter de la misma


def corrimiento_circular_izquierda(cadena) -> str:
    return cadena[1:]+cadena[0]


"""
cadena: str = "al sur de Colombia"
print(corrimiento_circular_izquierda(cadena))
"""
