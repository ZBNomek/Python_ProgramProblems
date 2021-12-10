# Hacer un algoritmo que calcule el M´aximo Com´un Divisor (MCD) para un arreglo de enteros
# positivos.

from E_22 import criba_de_eratostenes

arreglo: list = [5, 10, 15]
primos: list = [2, 3, 5]


def factorizacion(numero):
    factores = []
    primos = [2, 3, 5, 7]
    while True:
        for i in primos:
            if numero % i == 0:
                numero /= i
                factores.append(i)
        if numero == 1:
            break
    print(factores)


"""    if numero % primos[0] == 0:
        numero /= primos[0]
        factores.append(primos[0])
        print(factores)
        if numero == 1:
            pass
        else:
            if numero % primos[0] == 0:
                numero /= primos[0]
                factores.append(primos[0])
                print(factores)
            if numero == 1:
                pass
            else:
                if numero % primos[1] == 0:
                    numero /= primos[1]
                    factores.append(primos[1])
                if numero == 1:
                    pass
                else:
                    if numero % primos[3] == 0:
                        numero /= primos[3]
                        factores.append(primos[3])
                    if numero == 1:
                        pass
                    else:
                        pass
    else:
        pass
    print(factores)

"""
factorizacion(84)
