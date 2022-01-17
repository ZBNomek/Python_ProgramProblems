# 75. Desarrollar un algoritmo que determine si una cadena de caracteres es pal´ındrome. Una cadena
# se dice pal´ındrome si al invertirla es igual a ella misma.

from J_74 import invertir_cadena


def palindrome(cadena: str) -> bool:
    flag: bool
    cadena_invertida: str = invertir_cadena(cadena)

    if cadena == cadena_invertida:
        flag = True
    else:
        flag = False

    return flag


"""
cadena :str = "amor a roma"

print(palindrome(cadena))
"""
