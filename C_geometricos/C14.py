
"""
 Dadas la pendiente y el punto de corte de dos rectas,
 determinar si son paralelas, perpendi-culares o ninguna
 de las anteriores
"""

"""
 Linear Ecuation 
 y = mx + b {Where m is the slope and b is where the line cuts on axis y}
"""


def line_type(m1: float, b1: float, m2: float, b2: float) -> str:
    if m1 == m2:
        return "parallel"
    else:
        y: float = -1/(m1)
        if y == m2:

            return("perpendicular")
        else:
            return("none")


m1 = float(input("m = "))
b1 = float(input("b = "))

m2 = float(input("m = "))
b2 = float(input("b = "))

"""
y = 2x - 3
y = x + 5

2x + 3 = x + 5
2x + 3 - (+3) = x - (x) + 5
2x - (x) = 5 - (3)
x = 2

mx + b = mx + b

mx - mx = b - b

"""


print("The lines given are", line_type(m1, b1, m2, b2))
