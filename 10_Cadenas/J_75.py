# 76. Desarrollar un algoritmo que determina si una cadena de caracteres es frase pal´ındrome. Una
# cadena se dice frase pal´ındrome si la cadena al eliminarle los espacios es pal´ındrome.

from J_74 import invertir_cadena
from J_73 import quitar_espacios


def palindrome(cadena: str) -> bool:
    flag: bool
    cadena = quitar_espacios(cadena)
    cadena_invertida: str = invertir_cadena(cadena)

    if cadena == cadena_invertida:
        flag = True
    else:
        flag = False

    return flag


"""
cadena = "anula las alas a la luna"

print(palindrome(cadena))
"""
