# 78. Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de caracteres. El corrimiento circular a derecha de una cadena es poner el ´ultimo car´acter de la
# cadena como primer car´acter de la misma.

def corrimiento_circular_derecha(cadena) -> str:
    return cadena[:1]+cadena[0:-1]


"""
cadena: str = "al sur de Colombia"
print(corrimiento_circular_derecha(cadena))
"""
