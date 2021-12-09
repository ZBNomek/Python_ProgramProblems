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
