# 13. Dado un natural, determinar si es un n´umero de Fibonacci o no.

def fibonacci(num: int) -> bool:
    fibonacci_bool: bool = False
    a: int
    b: int
    c: int = 1
    n: int = (1, 1)

    while c <= num:
        if n[1] == num:
            fibonacci_bool: bool = True
            break
        else:
            a, b = n[0], n[1]
            c = a + b
            n = (b, c)
    return fibonacci_bool


"""
# Fibonacci True:
n1: int = 21

# Fibonnacci False
n2: int = 25

print(fibonacci(n1))  # ---> True
print(fibonacci(n2))  # ---> False
"""
