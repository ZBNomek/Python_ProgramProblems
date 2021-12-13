from typing import ContextManager
from z_checkers import *
from F_35 import union_conjuntos
from F_36 import interseccion_conjuntos
from F_37 import diferencia_conjuntos
from F_38 import diferencia_sim_conjuntos
from F_39 import pertenencia
from F_40 import contenido

"""
Aqui hay funciones que hacen display de los menus y le dan la funcionalidad a estos.

"""


def main_menu() -> bool:  # -> main_menu imprime la interfas del menu principal y devuelve un booleano que determina si el usuario quiere inicual/continuar el programa, o salir de este
    print("""

Main menu:

    Welcome to my program!!!
    This program does operations between 2 sets of numbers

        [1] Start
        [2] Exit
    """)

    switch: int = checker_options((1, 2), "int")
    end: bool

    if switch == 1:
        end = False
    else:
        end = True

    return end

# -> le da la oportunidad al usuario de crear un conjunto por medio de rangos, para que de esta manera no tenga que colocar consecutivos manualmente.


def range_set() -> tuple:
    while True:
        range_set_breaker = False
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
        # -> si el usuario esta satisfecho con el conjunto, continua con el programa
        print("Is this ok? [y/n]")

        y_n = checker_options(("y", "n"), "str")

        if y_n == "y":
            return_data = (True, set)
            range_set_breaker = True
        else:  # si no está satisfecho, el programa le da dos opciones al usuario -> volver al menu principal o volver al inicio de este loop para volver a colocar los valores del conjunto
            print("""Would you like to:
    [1] Set again the range for the set
    [2] Go back to the main menu
            """)
            retry = checker_options((1, 2), "int")
            if retry == 1:
                pass
            else:
                return_data = (False, [])
                range_set_breaker = True
        if range_set_breaker == True:
            break
    return return_data

# -> le da la oportunidad al usuario de crear un conjunto manuanlmente al usuario.


def custom_set() -> tuple:
    while True:
        set: list = []
        n: int = checker(
            "int", "Number of elements on the custom set: ")  # -> cuantos elementos tiene el conjunto para determinar cuantas veces hay quue repetir el loop de input
        print()
        print("Type below the elements you want to add to the set: (Press enter after typing each value)")
        for i in range(0, n):
            ele: int = checker("int", "> ")
            set.append(ele)
        print()
        print("Set:")
        print(set)
        print()
        # -> si el usuario esta satisfecho con el conjunto, continua con el programa
        print("Is this ok? [y/n]")
        y_n = checker_options(("y", "n"), "str")

        if y_n == "y":
            return_data = (True, set)
            break
        # si no está satisfecho, el programa le da dos opciones al usuario -> volver al menu principal o volver al inicio de este loop para volver a colocar los valores del conjunto
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

# -> determina si el suario quiere ingresar un conjunto por medio de la funcion de rango o personalizada


def set_set() -> tuple:
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

# operations imprime el interfas del menu de posibles operaciones con los conjuntos y realiza las respectivas operacoines, usando funciones de ejercicios anteriores


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

    # dependiendo de el numero ingresado hace la operacion correspondiente
    if a == 1:
        print("A ∪ B = ", union_conjuntos(A, B))
    elif a == 2:
        print("A ∩ B = ", interseccion_conjuntos(A, B))
    elif a == 3:
        print("A - B =", diferencia_conjuntos(A, B))
        print("B - A =", diferencia_conjuntos(B, A))
    elif a == 4:
        print("A Δ B = ", diferencia_sim_conjuntos(A, B))
    elif a == 5:
        print("Type below the number you want to find if it belong's to one of the sets: ")
        n: int = checker("int", "> ")
        print()
        print("Is", n, "in A? -> ", pertenencia(n, A, B)[0])
        print("Is", n, "in B? ->", pertenencia(n, A, B)[1])

    elif a == 6:
        print("Is A a subset of B? -> ", contenido(A, B))
        print("Is B a subset of A? -> ", contenido(B, A))
    print()

# -> booleano destinado a que dependiento del input del usuario, repite el menu de operaciones o regresa al menu principal.


def repetition() -> bool:
    print("Do you want to do another operation with the same sets? [y/n]")
    a = checker_options(("y", "n"), "str")
    if a == "y":
        return True
    else:
        return False
