import defs.program_defs as prog

while True:
    while True:
        breaker = False
        end_program: bool = prog.main_menu()
        if end_program == True:
            breaker = True
            break
        else:
            print()
            print("Set 1:")
            A = prog.set_set()
            if A[0] == False:
                break
            else:
                A = A[1]
            print()
            print("Set 2:")
            B = prog.set_set()
            if B[0] == False:
                break
            else:
                B = B[1]
            while True:
                prog.operations(A, B)
                if prog.repetition() == False:
                    break
                else:
                    pass
    if breaker == True:
        break
