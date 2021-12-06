
def prime_check(num: int) -> bool:
    prime: bool = True
    if num > 1:
        if num == 2:
            None
        else:
            for i in [2, num+1]:
                if (num % i) == 0:
                    prime = False
                    break
    return prime


input1: int = int(input("Number = "))
prime: bool = prime_check(input1)
if prime:
    print(input1, " is a prime number.")
else:
    print(input1, " is not a prime number.")
