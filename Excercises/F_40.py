# 40. Contenido: Determina s´ı el primer conjunto esta contenido en el segundo y lo imprime.

def contenido(conjunto_a: list, conjunto_b: list) -> bool:
    contenido: bool = True
    for i in conjunto_a:
        if i not in conjunto_b:
            contenido = False
            break
    return contenido


"""
conjunto_a: list = [1, 2, 3, 4, 5]
conjunto_b: list = [2, 3, 4]

# contenido
print(contenido(conjunto_b, conjunto_a))

# no contenido
print(contenido(conjunto_a, conjunto_b))
"""
