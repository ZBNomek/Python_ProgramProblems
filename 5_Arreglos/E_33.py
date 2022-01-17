# Hacer un algoritmo que calcule el M´aximo Com´un Divisor (MCD) para un arreglo de enteros
# positivos.

from E_22 import criba_de_eratostenes
from E_27 import max_elem
from E_28 import producto_directo_elem
from others import ordenar_valores


# Funcion para sacar los numeros primos de la factorizacion de 1 un numero
def factorizacion(numero) -> list:
    factores = []
    primos = criba_de_eratostenes(numero)
    while True:
        for i in primos:
            if numero % i == 0:
                numero /= i
                factores.append(i)
        if numero == 1:
            break
    factores = ordenar_valores(factores)
    return factores


# Función que da la cantidad de cada numero primo en la factorizacion de un numero -> factorizacion de 50 = [2,5,5] | la funcion devolveria = [1,0,2] ya que hay 1 dos, 0 treces y 2 cincos. llega hasta el cinco ya que es el numero maximo dado.
def cantidad_primos_en_conjunto(factores: list, numero_maximo: list) -> list:
    numeros_primos = criba_de_eratostenes(numero_maximo)
    temp_list_2 = []
    lenght = len(numeros_primos)
    c = 0
    while lenght > 0:
        t = 0
        for i in factores:
            if i == numeros_primos[c]:
                t += 1
        c += 1
        temp_list_2.append(t)
        lenght -= 1
    return temp_list_2


# compara dos listas y de cada indice correspondiente, escoge el menor valor ya que es el que comparten. (maximo numero primo en comun)
def union_factores(factores_1: list, factores_2: list) -> list:
    lista_factores = []
    t = 0
    for i in factores_1:
        if i > factores_2[t]:
            lista_factores.append(factores_2[t])
        else:
            lista_factores.append(i)
        t += 1

    return lista_factores


# recibe una lista con una cantidad que le corresponde a la cantidad de numeros primos, y en base a eso los multiplica para obtener un numero completo.
def primos_a_decimal(primos: list) -> int:
    temp_primos = []
    n = 2
    while True:
        temp_primos = criba_de_eratostenes(n)
        if len(temp_primos) == len(primos):
            break
        else:
            n += 1

    temp_primos = producto_directo_elem(temp_primos, primos)
    a = 1
    for i in temp_primos:
        if i != 0:
            a *= i

    return a


# Funcion para obtener el maximo comun divisor de los digitos en una lista
def max_comun_div(conjunto: list) -> int:
    temp_list = []
    temp_valores = []
    temp_list_2 = []
    for i in conjunto:  # Saco la factorizaciond de cada numero y la almaceno una lista
        factores = factorizacion(i)
        temp_list.append(factores)
    for i in temp_list:  # Saco el maximo valor primo de entre todas las factoricaciones.
        maximo_valor = max_elem(i)
        temp_valores.append(maximo_valor)
    maximo_valor = max_elem(temp_valores)
    for i in temp_list:  # Obtiene la cantidad de numeros primos que conforma cada de cada numero
        temp_list_2.append(cantidad_primos_en_conjunto(i, maximo_valor))
    temp_list = [*temp_list_2]
    temp_list_2 = temp_list[0]

    for i in temp_list[1:]:  # busca el maximo numero primo en comun de cada numero primo
        temp_list_2 = union_factores(temp_list_2, i)

    # devuelve los primos obtenido en forma de un numero completo.
    return primos_a_decimal(temp_list_2)


"""
conjunto = [12, 20, 14, 124, 72, 2458]
print(max_comun_div(conjunto))
"""
"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

a = factorizacion(210)
b = factorizacion(50)
max_ = max_elem([max_elem(a), max_elem(b)])
aa = cantidad_elem_en_conjunto(a, max_)
bb = cantidad_elem_en_conjunto(b, max_)
print(aa, bb)
e = union_factores(aa, bb)
primos_a_decimal(e)

        if numero % primos[0] == 0:
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
