from G_44 import igualar_polinomios


def suma_lista(lista: list):
    a: int = 0
    for i in lista:
        a += i
    return a


def analisis_polinomio(polinomio, f):
    c = f

    temp = []
    n = 0
    for i in polinomio:
        c = f
        res = (len(polinomio) - n)-1
        if res > 0:
            c = c ** res
        else:
            c = 1
        temp.append(c)
        n += 1
    for i in polinomio:
        polinomio[polinomio.index(i)] *= temp[polinomio.index(i)]

    return suma_lista(polinomio)


n = 3
polinomio_1 = [2, 1, -3]  # 2x^2 + x - 3 = 2(3)^2 + (3) - 3 = 18
polinomio_2 = [1, -3, -1]  # x^2 - 3x + 1 = (3)^2 - 3(3) + 1 = -1

print(">", analisis_polinomio(polinomio_1, n))
print(">", analisis_polinomio(polinomio_2, n))
