import math
from typing import Union


def ploynomial_analysis(a: float, b: float, c: float) -> Union[bool, tuple]:
    flag: bool = False
    p1: float = (b**2)-(4*a*c)
    p2: float = 2*a
    if p1 < 0 or p2 <= 0:
        flag = True
    else:
        x1: float = (-b+math.sqrt(p1))/p2
        x2: float = (-b-math.sqrt(p1))/p2
    if flag:
        return False
    else:
        return (x1, x2)


print("----> ax^2 + bx + c <----")
input1: int = int(input("a = "))
input2: int = int(input("b = "))
input3: int = int(input("c = "))
polynomial: bool = ploynomial_analysis(input1, input2, input3)
if polynomial:
    print("The answers are = ", polynomial[0], " and ", polynomial[1])
else:
    print("The polynomial has no answer... at least one that can be found through the cuadratic formula.")
