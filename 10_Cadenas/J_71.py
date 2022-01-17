# 71. Desarrollar un algoritmo que reciba como entrada un car´acter y de como salida el n´umero de
# ocurrencias de dicho car´acter en una cadena de caracteres.

def n_en_cadena(cadena: str, caracter: str) -> int:

    n: int = 0

    for i in cadena:
        if caracter == i:
            n += 1

    return n


cadena: str = "hipopotamo"
caracter: str = "o"

print(n_en_cadena(cadena, caracter))
