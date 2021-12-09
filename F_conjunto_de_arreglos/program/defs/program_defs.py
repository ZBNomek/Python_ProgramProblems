from defs.checkers import checker, checker_options
import defs.operation_defs as op


def main_menu():
    print("""

Main menu:

    Welcome to my program!!!
    This program does operations between 2 sets of numbers

        [1] Start
        [2] Exit
    """)

    temp: int = checker_options((1, 2), "int")
    start: bool

    if temp == 1:
        end = False
    else:
        end = True

    return end


def range_set():
    while True:
        breaker = False
        print("Select the range for the set of numbers")
        a1: int = checker("int", "From number: ")
        a2: int = checker("int", "To number: ")
        aStep: int = checker("int", "Step between numbers: ")
        print()

        a2 += 1

        set: list = [*range(a1, a2, aStep)]

        print("Set: ")
        print(set)
        print()
        print("Is this ok? [y/n]")

        y_n = checker_options(("y", "n"), "str")

        if y_n == "y":
            return_data = (True, set)
            breaker = True
        else:
            print("""Would you like to:
    [1] Set again the range for the set
    [2] Go back to the main menu
            """)
            retry = checker_options((1, 2), "int")
            if retry == 1:
                pass
            else:
                return_data = (False, [])
                breaker = True
        if breaker == True:
            break
    return return_data


def custom_set():
    while True:
        set: list = []
        n: int = checker(
            "int", "Number of elements on the custom set: ")
        print()
        print("Type below the elements you want to add to the set: (Press enter after typing each value)")
        for i in range(0, n):
            ele = checker("int", "> ")
            set.append(ele)
        print()
        print("Set:")
        print(set)
        print()
        print("Is this ok? [y/n]")
        y_n = checker_options(("y", "n"), "str")

        if y_n == "y":
            return_data = (True, set)
            break
        else:
            print("[1] Set again the ranges for the sets")
            print("[2] Go back to the main menu")
            retry = checker_options((1, 2), "int")
            if retry == 1:
                pass
            else:
                return_data = (False, ())
                breaker = True
                break
    return return_data


def set_set():
    print("""  For this set wolud you like a range of values or a custom set
        [1] Range
        [2] Custom
    """)

    temp: int = checker_options((1, 2), "int")
    print()
    if temp == 1:
        set = range_set()
    elif temp == 2:
        set = custom_set()
    return set


def operations(A: list, B: list):
    print("Set A = ", A)
    print("Set B = ", B)
    print("""
Program Options:
    [1] Union
    [2] Intersection
    [3] Difference
    [4] Symetric Difference
    [5] Belonging
    [6] Subset
    
Type below an option of the menu
    """)

    a = checker_options((1, 2, 3, 4, 5, 6), "int")

    print()
    print("A: ", A)
    print("B: ", B)
    print()

    if a == 1:
        print("A ∪ B = ", op.union_conjuntos(A, B))
    elif a == 2:
        print("A ∩ B = ", op.interseccion_conjuntos(A, B))
    elif a == 3:
        temp = op.diferencia_conjuntos(A, B)
        print(temp[0][0], temp[0][1])
        print(temp[1][0], temp[1][1])
    elif a == 4:
        print("A Δ B = ", op.diferencia_sim_conjuntos(A, B))
    elif a == 5:
        temp = op.pertenencia(A, B)
        print(temp[0], " AND ", temp[1])
    elif a == 6:
        temp = op.contenido(A, B)
        print(temp[0], " AND ", temp[1])
    print()


def repetition():
    print("Do you want to do another operation with the same sets? [y/n]")
    a = checker_options(("y", "n"), "str")
    if a == "y":
        return True
    else:
        return False
