def decimal_a_binario(decimal: int):
    bits = []
    t = 0
    while True:
        if pow(2, t) <= decimal:
            t += 1
        else:
            t -= 1
            break
    while t >= 0:
        multiplicador = pow(2, t)
        if multiplicador <= decimal:
            decimal -= pow(2, t)
            bits.append(1)
        else:
            bits.append(0)
        if multiplicador <= decimal:
            pass
        else:
            t -= 1
    return bits[::-1]


"""
decimal_1: int = 106  # ---> [0, 1, 0, 1, 0, 1, 1]
decimal_2: int = 489  # ---> [1, 0, 0, 1, 0, 1, 1, 1, 1]

print(decimal_1, " = ", decimal_a_binario(decimal_1))
print(decimal_2, " = ", decimal_a_binario(decimal_2))
"""
