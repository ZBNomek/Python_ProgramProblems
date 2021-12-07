n: int = 37
numbers_list: list
flag: bool
iden: int = 0

# 1 will never be a prime number, so the range starts in 2
numbers_list = [*range(2, n+1)]
flag = True
c = 0
iden = numbers_list[c]
while flag == True:
    print("iden", iden)
    for n in numbers_list:
        if n == iden:
            pass
        elif n % iden == 0:
            numbers_list.remove(n)
    print(numbers_list)

    flag2 = True

    while flag2 == True:
        iden += 1
        for n in numbers_list:
            if iden == n:
                flag2 = False
            else:
                pass

    print("iden", iden)
    for n in numbers_list:
        if pow(iden, 2) == n:
            flag = True
            break
        else:
            flag = False

    print(iden)
    print(pow(iden, 2))
    print(flag)
