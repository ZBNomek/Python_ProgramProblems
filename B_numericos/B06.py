from typing import Union


def division_check(dividend: int, divisor: int) -> Union[int, bool]:
    if ((dividend % divisor) == 0):
        division: int = dividend/divisor
        return True, division
    else:
        return False, False


input1: int = int(input("Dividend = "))
input2: int = int(input("Divisor = "))
data: tuple = division_check(input1, input2)
if data[0]:
    print(input1, " divided by ", input2, " can be bivided without residue.")
    print("Answer = ", data[1])
else:
    print(input1, " divided by ", input2,
          " can not be bivided without residue.")
