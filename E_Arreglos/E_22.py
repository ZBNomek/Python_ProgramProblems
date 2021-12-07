
def criba_de_eratostenes(n: int) -> list:
    numbers_list: list
    flag: bool
    iden: int = 0

    # 1 will never be a prime number, so the range starts in 2
    numbers_list = [*range(2, n+1)]
    flag = True
    c = 0
    iden = numbers_list[c]
    while flag == True:
        for n in numbers_list:
            if n == iden:
                pass
            elif n % iden == 0:
                numbers_list.remove(n)
        flag2 = True

        while flag2 == True:
            iden += 1
            for n in numbers_list:
                if iden == n:
                    flag2 = False
                else:
                    pass
        for n in numbers_list:
            if pow(iden, 2) == n:
                flag = True
                break
            else:
                flag = False

    return numbers_list


number: int = int(input("Encontrar los numeros primos desde 1 hasta => "))
print(criba_de_eratostenes(number))

"""
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
