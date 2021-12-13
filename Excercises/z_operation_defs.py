from z_checkers import checker
from B_08 import ordenar_valores

# no se muy bien como funciona esto delos paquetes aun asi que copie los ejercicios acá


def union_conjuntos(conjunto_a: list, conjunto_b: list) -> list:
    lista_union: list = []
    for i in conjunto_a:
        lista_union.append(i)
    for i in conjunto_b:
        if i not in conjunto_a:
            lista_union.append(i)
    return ordenar_valores(lista_union)


# 36. Intersecci´on: Calcula en un arreglo la intersecci´on de los conjuntos y la imprime.


def interseccion_conjuntos(a: list, b: list):
    temp: list = []
    for i in a:
        if i in b:
            temp.append(i)
        else:
            pass
    return temp

# 37. Diferencia: Calcula en un arreglo la diferencia del primero con el segundo y la imprime.


def diferencia_conjuntos(a: list, b: list):
    temp: list = []
    temp2: list = []
    for i in a:
        if i not in b:
            temp.append(i)
    temp = ["A - B = ", temp]
    temp2.append(temp)
    temp: list = []
    for i in b:
        if i not in a:
            temp.append(i)
    temp = ["B - A = ", temp]
    temp2.append(temp)
    return temp2


# 38. Diferencia sim´etrica: Calcula en un arreglo la diferencia sim´etrica de los conjuntos y la
# imprime.


def diferencia_sim_conjuntos(a: list, b: list):
    diff: list = diferencia_conjuntos(a, b)
    temp: list = union_conjuntos(
        diff[0][1], diff[1][1])
    return temp


# 39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los
# conjuntos y lo imprime.


def pertenencia(a: list, b: list):
    n_in_a: bool = False
    n_in_b: bool = False
    temp: list = []

    print("Type a number to find in set A or B: ")
    n = checker("int", "> ")
    print()

    for i in a:
        if n == i:
            n_in_a = True
            break
        else:
            pass
    for i in b:
        if n == i:
            n_in_b = True
            break
        else:
            pass

    if n_in_a == True:
        temp.append(str(n) + " ϵ A")
    else:
        temp.append(str(n) + " ∉ A")
    if n_in_b == True:
        temp.append(str(n) + " ϵ B")
    else:
        temp.append(str(n) + " ∉ B")

    return temp

# 40. Contenido: Determina s´ı el primer conjunto esta contenido en el segundo y lo imprime.


def contenido(a: list, b: list):
    a_in_b: bool
    b_in_a: bool
    lenght: bool = True if len(a) == len(b) else False
    temp: list = []

    for i in a:
        if i not in b:
            a_in_b = False
            break
        else:
            a_in_b = True
            if len(a) == len(b):
                ab = True
            else:
                ab = False
    for i in b:
        if i not in a:
            b_in_a = False
            break
        else:
            b_in_a = True

    if a_in_b == True:
        if lenght == True:
            temp.append("A ⊆ B")
        else:
            temp.append("A ⊂ B")
    else:
        temp.append("A ⊄ B")

    if b_in_a == True:
        if lenght == True:
            temp.append("B ⊆ A")
        else:
            temp.append("B ⊂ A")
    else:
        temp.append("B ⊄ A")

    return temp
