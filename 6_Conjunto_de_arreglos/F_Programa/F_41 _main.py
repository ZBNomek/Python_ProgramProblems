from program_functions import *

"""
Programa que permite hacer operaciones con dos conjuntos, dandole un menu al usuario en el cual solo sale del programa cuando el usuario lo desee
En este main.py se le da un orden a las partes del programa y se crean los loops de las partes del programa.

------> Lo hice en ingles sin querer, caí en cuenta muy tarde <------
"""

while True:
    while True:
        program_breaker: bool = False
        # main menu where you can choose to continue the program or exit
        end_program: bool = main_menu()
        if end_program == True:
            program_breaker = True
            break
        # if exit == false -> continue with the program
        else:
            print()
            print("Set 1:")
            A: tuple = set_set()  # -> set the first det of numbers
            # if the user wants to go to the main menu, break the program loop. (A is equal to a tuple that contains a boolean that determines if the user wants to go to the main menu, and a lists with the set)
            if A[0] == False:
                break
            else:
                # -> if the user wants to continue, the tuple is deleted and A now only stores the information of the set.
                A: list = A[1]
            print()
            print("Set 2:")
            # -> repeats process done with the first set for the second set.
            B: tuple = set_set()
            if B[0] == False:
                break
            else:
                B: list = B[1]
            while True:
                # -> menu for the operations with sets
                operations(A, B)
                # when the user wants to go to the main menu, this while loop breaks.
                if repetition() == False:
                    break
    if program_breaker == True:
        break
