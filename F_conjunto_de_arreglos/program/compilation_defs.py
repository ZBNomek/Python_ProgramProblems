# 35. Uni´on: Calcula en un arreglo la uni´on de los conjuntos y la imprime


def union_conjuntos(a: list, b: list):
    temp: list = []
    for i in a:
        temp.append(i)
    for i in b:
        if i not in a:
            temp.append(i)
    return temp

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
    for i in a:
        if i not in b:
            temp.append(i)
        else:
            pass
    return temp


# 38. Diferencia sim´etrica: Calcula en un arreglo la diferencia sim´etrica de los conjuntos y la
# imprime.


def diferencia_sim_conjuntos(a: list, b: list):
    temp: list = union_conjuntos(
        diferencia_conjuntos(a, b), diferencia_conjuntos(b, a))
    print(union_conjuntos(
        diferencia_conjuntos(a, b), diferencia_conjuntos(b, a)))
    return temp

# 39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los
# conjuntos y lo imprime.


def pertenencia(n: int, a: list, b: list):
    flag_a: bool = False
    flag_b: bool = False
    temp: list
    for i in a:
        if n == i:
            flag_a = True
            break
        else:
            pass
    for i in b:
        if n == i:
            flag_b = True
            break
        else:
            pass
    temp = [flag_a, flag_b]
    return temp

# 40. Contenido: Determina s´ı el primer conjunto esta contenido en el segundo y lo imprime.


def contenido(a: list, b: list):
    flag: bool = True
    for i in a:
        if i not in b:
            flag = False
            break
        else:
            pass
    temp = flag
    return temp
