decimal_1: int = 106
decimal_2: int = 235


def decimal_a_binario(decimal: int):
    bits = []
    n = 0
    while True:
        if pow(2, n) <= decimal:
            n += 1
        else:
            n -= 1
            break
    while n >= 0:
        multiplicador = pow(2, n)
        if multiplicador <= decimal:
            decimal -= pow(2, n)
            bits.append(1)
        else:
            bits.append(0)
        if multiplicador <= decimal:
            pass
        else:
            n -= 1
    return bits[::-1]


#print(decimal_1, " = ", decimal_a_binario(decimal_1))
#print(decimal_2, " = ", decimal_a_binario(decimal_2))
