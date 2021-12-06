def fibonacci_check(num: int) -> bool:
    flag: bool = False
    a: int
    b: int
    c: int = 1
    n: int = (1, 1)

    while c <= num:
        if n[1] == num:
            flag: bool = True
            break
        else:
            a, b = n[0], n[1]
            c = a + b
            n = (b, c)
        print(n[0], n[1])
    if flag:
        return True
    else:
        return False

# print(fibonacci_check(21))
