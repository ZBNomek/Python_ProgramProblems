from typing import Union
from B7 import prime_check


def relative_prime(num_a: int, num_b: int) -> bool:
    relative: bool = True
    if num_a < num_b:
        num_a, num_b = num_b, num_a
    for i in range(2, num_a):
        prime = prime_check(i)
        if prime == True:
            if (num_a % i) == 0:
                num_a = num_a/i
                if (num_b % i) == 0:
                    relative = False
                    break
    return relative


input1: int = int(input("Number 1 = "))
input2: int = int(input("Number 2 = "))
prime_relative: bool = relative_prime(input1, input2)
if prime_relative:
    print(input1, " and ", input2, " are relatively prime numbers")
else:
    print(input1, " and ", input2, " are not relatively prime numbers")
