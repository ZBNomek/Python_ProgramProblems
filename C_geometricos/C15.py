def intersection(m1: float, b1: float, m2: float, b2: float) -> tuple:
    x = (b2-b1)/(m1-m2)
    y = (m1 * x) + b1
    return (x, y)


m1 = float(input("m = "))
b1 = float(input("b = "))

m2 = float(input("m = "))
b2 = float(input("b = "))

print("The intersection point for the lines given is",
      intersection(m1, b1, m2, b2))
