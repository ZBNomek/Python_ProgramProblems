# 10. Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado.

def polinomio_grad_2(a: int, b: int, c: int) -> tuple:
    discriminante: float = (b**2) - (4*a*c)
    if discriminante > 0:
        x1: float = (-b + (discriminante**0.5))/(2*a)
        x2: float = (-b - (discriminante**0.5))/(2*a)
        return x1, x2
    else:
        return None, None


"""
# Polinomio grado 2 = a^2 + b + c
a: int = -5
b: int = 1
c: int = 6

print(polinomio_grad_2(a, b, c))
"""
