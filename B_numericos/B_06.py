# 6. Una funci´on que determine si un n´umero es divisible por otro.

def divisible(dividend: int, divisor: int) -> bool:
    divisible: bool
    if dividend % divisor == 0:
        divisible = True
    else:
        divisible = False

    return divisible


"""
dividendo: int = 15
divisor: int = 5
print(divisible(15, 5))
"""
