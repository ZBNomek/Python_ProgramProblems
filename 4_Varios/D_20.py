# 20. Si un amigo, no tan amigo, me presta K pesos a i pesos de inter´es diario, ¿cu´anto le pagar´e
# en una semana si el inter´es es simple?, ¿y cu´anto si el inter´es es compuesto?.


def interes_simple(k: float, i: float) -> float:
    deuda: float = (k+i)*7
    return deuda


def interes_compuesto(k: float, i: float) -> float:
    deuda: float = k * (pow((1+(i/k)), 7))
    return deuda


"""
print(interes_simple(1000, 500)) # 1000 pesos de prestamo con 500 de interes diario
print(interes_compuesto(1000, 500)) 
"""
