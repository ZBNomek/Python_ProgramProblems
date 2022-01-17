# 74. Desarrollar un algoritmo que invierta una cadena de caracteres.

def invertir_cadena(cadena: str) -> str:
    cadena_invertida: str = ""

    for i in cadena:
        cadena_invertida = i+cadena_invertida

    return cadena_invertida


"""
cadena = "cadena de caracteres"
print(invertir_cadena(cadena))
"""
