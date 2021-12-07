"""
20. Si un amigo, no tan amigo, me presta K pesos a i pesos de inter´es diario, ¿cu´anto le pagar´e
en una semana si el inter´es es simple?, ¿y cu´anto si el inter´es es compuesto?.

"""


def interes_simple(k: float, i: float):
    a = (k+i)*7
    return a


def interes_compuesto(k: float, i: float):
    a = k * (pow((1+(i/k)), 7))
    return a


print(interes_simple(1000, 500))
print(interes_compuesto(1000, 500))
