# 73. Desarrollar un algoritmo que reciba dos cadenas de caracteres y determine si la primera est´a
# incluida en la segunda. Se dice que una cadena est´a incluida en otra, si todos los caracteres
# (con repeticiones) de la cadena est´a en la segunda cadena sin tener en cuenta el orden de los
# caracteres.


def quitar_espacios(cadena: str) -> str:
    return cadena.replace(" ", "")


def sub_cadena_desordenada_en_cadena(cadena: str, sub_cadena: str) -> bool:
    cadena = quitar_espacios(cadena)
    sub_cadena = quitar_espacios(sub_cadena)

    n: int = len(sub_cadena)
    flag: bool = True
    breaker: bool = True

    while 0 < n:
        if flag == False:
            break
        for i in sub_cadena:
            for e in cadena:
                if i == e:
                    cadena = cadena.replace(e, "", 1)
                    sub_cadena = sub_cadena.replace(i, "", 1)
                    flag = True
                    breaker = True
                    break
            else:
                flag = False
                breaker = True
        if breaker == True:
            break
    n -= 1

    return flag


"""
cadena = "la profesora de ingles"
sub_cadena = "prosa"

print(sub_cadena_desordenada_en_cadena(cadena, sub_cadena))
"""
