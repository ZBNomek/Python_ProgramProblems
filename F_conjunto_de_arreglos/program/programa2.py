from compilation_defs import all

print("Welcome to my program!!!")
print()

main_loop = True

while main_loop == True:
    flag = True
    while flag == True:

        print("Menu: ")
        print("[1] Sets with ranges")
        print("[2] Custom sets")
        print()
        print("Type an option of the menu")
        type_of_sets = input(">>> ")

        try:
            type_of_sets = int(type_of_sets)
            if (type_of_sets == 1 or type_of_sets == 2):
                flag = False
            else:
                print("not valid")
                print()
        except:
            ValueError
            print("not valid")
            print()
    print("gut")
"""
    print("Select the first set of numbers")
    a1: int = int(input("From: "))
    a2: int = int(input("To: "))
    aStep: int = int(input("Step: "))
    print()
    print("Select the second set of numbers")
    b1: int = int(input("From: "))
    b2: int = int(input("To: "))
    bStep: int = int(input("Step: "))
    print()

    a2 += 1
    b2 += 1

    A: list = [*range(a1, a2, aStep)]
    B: list = [*range(b1, b2, bStep)]

    print("Set 1: ")
    print(A)
    print()
    print("Set 2:")
    print(B)
    print()

    
"""
