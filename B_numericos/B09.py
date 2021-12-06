

def multiple_of_addition(num_sum1: int, num_sum2: int, num_multiple: int) -> bool:
    multiple = False
    suma = num_sum1+num_sum2
    if suma < num_multiple and (num_multiple % suma) == 0:
        multiple = True
    return multiple


input1: int = int(input("Number 1 for addition = "))
input2: int = int(input("Number 2 for addition = "))
input3: int = int(input("Number for multiple check = "))
multiple = multiple_of_addition(input1, input2, input3)
if multiple:
    print("The sum of ", input1, " and ", input2, " is a multiple of ", input3)
else:
    print("The sum of ", input1, " and ", input2,
          " is not a multiple of ", input3)
