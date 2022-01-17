# 8. Dados dos naturales, determinar si son primos relativos.

from B_07 import primo


def ordenar_valores(arreglo: list) -> list:
    arreglo_ordenado: list = [0]*len(arreglo)
    for i in arreglo:
        t: int = 0
        for e in arreglo:
            if i <= e:
                t += 1
            else:
                pass
        arreglo_ordenado[-t] = i
    for i in arreglo_ordenado:
        if i == 0:
            arreglo_ordenado[arreglo_ordenado.index(
                i)] = arreglo_ordenado[arreglo_ordenado.index(
                    i)-1]
    return arreglo_ordenado

# n = numero al que se le buscan los numeros de su factorización


def factorizacion(n) -> list:
    valores: list = []
    while True:
        rango: list = [*range(2, int(n)+1)]
        while len(rango) > 0:
            if (primo(rango[0]) == True) and (n % rango[0] == 0):
                valores.append(rango[0])
                break
            del rango[0]
        n /= valores[-1]
        if n == 1:
            break
    return valores


def primos_relativos(numero_1: int, numero_2: int) -> bool:
    factores_n1: list
    factores_n2: list
    primos: bool = True
    if (primo(numero_1) == True) and (primo(numero_2) == True):
        pass
    else:
        factores_n1 = ordenar_valores(factorizacion(numero_1))
        factores_n2 = ordenar_valores(factorizacion(numero_2))
        for i in factores_n1:
            for e in factores_n2:
                if i == e:
                    primos = False
    return primos


"""
#Son relativos:
r1:int = 99
r2:int  = 101

#No son relativos
n1:int  = 5
n2:int  = 15

print(primos_relativos(101, 99)) # ---> relativos
print(primos_relativos(101, 99)) # ---> no relativos
"""
