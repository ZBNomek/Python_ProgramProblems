# Implementar la criba de Eratostenes para calcular los n´umeros primos en el rango 1 a n, donde
# n es un n´umero natural dado por el usuario.

def criba_de_eratostenes(n: int) -> list:
    lista_de_numeros: list
    flag: bool
    index: int = 0

    """
    # 1 nunca va a ser un numero primo devido ya
    que por regla tedria que ser divisible por 2 
    numeros (1 y el mismo), por lo que lo dejo 
    por fuera por practicidad.
    """

    # ---> Lsita de numeros entre 2 y el numero dado
    lista_de_numeros = [*range(2, n+1)]
    continue_flag = True
    i = 0
    index = lista_de_numeros[i]

    while continue_flag == True:
        for n in lista_de_numeros:  # ---> Para cada cada nimero en orden, se eliminan los multiplos de este de la lista, ya que no seria primos
            # El primer multiplo de un numero no se borra...
            if n == index:
                pass  # ------------->  por lo que no hace nada el programa.
            # Para el resto de elementos, si se divindex sin residuo por el primer digito...
            elif n % index == 0:
                # se quita de la lista ya que no es primo.
                lista_de_numeros.remove(n)

        index += 1

        for n in lista_de_numeros:
            # Si la potencia de dos del numero que sigue se encuentra en la lista significa que quedan digitos no primos en la lista.
            if pow(index, 2) == n:
                continue_flag = True
                break
            else:
                # Si la potencia no se encuentra, no hay mas numeros primos y se acaba el looop principal.
                continue_flag = False

    return lista_de_numeros


"""
n: int = 20
print(criba_de_eratostenes(n))
"""

"""
---> Me da pesar borrar lo de abajo :_c <---

number: int = int(input("Encontrar los numeros primos desde 1 hasta => "))
print(criba_de_eratostenes(number))

lst: list = [*range(2, n+1)]
lst_prime: list = []
lst_prime.append(lst[0])
lst_remove: list = []
print()
print(lst)
print(lst_prime)
print()
for i in lst:
    if i % lst[0] == 0:
        lst_remove.append(i)
print()
print(lst_remove)
print(lst)
print(lst_prime)
print()
for i in lst_remove:
    a = i
    print("-->", a)
    lst.remove(a)
print()
print(lst_remove)
print(lst)
print(lst_prime)
print()
flag: bool
u = lst[0]
for i in lst:
    if pow(u, 2) == i:
        flag = True
        break
    else:
        flag = False
print(flag)
if flag == True:
    lst_prime.append(lst[0])
    lst_remove: list = []
    print()
    print(lst)
    print(lst_prime)
    print()
    for i in lst:
        if i % lst[0] == 0:
            lst_remove.append(i)
    print()
    print(lst_remove)
    print(lst)
    print(lst_prime)
    print()
    for i in lst_remove:
        a = i
        print("-->", a)
        lst.remove(a)
    print()
    print(lst_remove)
    print(lst)
    print(lst_prime)
    print()
else:
    pass
u = lst[0]
for i in lst:
    if pow(u, 2) == i:
        flag = True
        break
    else:
        flag = False
print(flag)
if flag == True:
    lst_prime.append(lst[0])
    lst_remove: list = []
    print()
    print(lst)
    print(lst_prime)
    print()
    for i in lst:
        if i % lst[0] == 0:
            lst_remove.append(i)
    print()
    print(lst_remove)
    print(lst)
    print(lst_prime)
    print()
    for i in lst_remove:
        a = i
        print("-->", a)
        lst.remove(a)
    print()
    print(lst_remove)
    print(lst)
    print(lst_prime)
    print()
else:
    pass
"""
