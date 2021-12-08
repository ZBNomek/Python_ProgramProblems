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
