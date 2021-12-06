from typing import Union
import math

# 5. Función potencia de un entero elevado a un entero.


def potencia(a: int, b: int) -> int:
    x: float
    if b == 0:
        x = 1
    else:
        x = pow(a, b)
    return x


print(potencia(2, -2))


def integer_pow(base: int, exponent: int) -> int:
    powr = pow(base, exponent)
    return powr


# Integer_pow test
'''
input1: int = int(input("Base = "))
input2: int = int(input("Exponent = "))
print("Result = ", integer_pow(input1, input2))
'''
