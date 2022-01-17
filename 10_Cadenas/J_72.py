# 72. Desarrollar un algoritmo que reciba como entrada dos cadenas y determine si la primera es
# subcadena de la segunda. (No se deben usar operaciones de subcadenas propias del lenguaje
# de programaci´on).


def separar_palabras(cadena: str) -> list:
    cadena_dividida: list = []
    temp: str = ""
    for i in cadena:
        if i == " ":
            cadena_dividida.append(temp)
            temp = ""
        else:
            temp += i

    if temp:
        cadena_dividida.append(temp)

    for i in cadena_dividida:
        if i == "":
            cadena_dividida.remove(i)

    return cadena_dividida


def sub_cadena_en_cadena(cadena: str, sub_cadena: str) -> bool:

    cadena_separada: list = separar_palabras(cadena)

    flag: bool
    for i in cadena_separada:
        if sub_cadena == i:
            flag = True
            break
        else:
            flag = False
    return flag


def print_result(cadena: str, sub_cadena: str, flag: bool) -> None:
    if flag == True:
        print(">>> La cadena '", sub_cadena,
              "' es subcadena de la cadena '", cadena, "'")
    else:
        print(">>> La cadena '", sub_cadena,
              "' es subcadena de la cadena '", cadena, "'")


cadena: str = "la prosa debe ser armoniosa"
sub_cadena: str = "prosa"
flag = sub_cadena_en_cadena(cadena, sub_cadena)

print_result(cadena, sub_cadena, flag)
