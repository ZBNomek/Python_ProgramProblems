"""while True:
    a = input()
    print(type(a))
"""


def checker_options(options: tuple, data_type: str):
    while True:
        validation_datatype: bool
        validation_option: bool

        a = input(">>> ")
        print()

        if data_type == "int":
            try:
                a = int(a)
                validation_datatype = True
                for i in options:
                    if a == i:
                        validation_option = True
                        break
                    else:
                        validation_option = False
            except:
                ValueError
                validation_datatype = False
        elif data_type == "str":
            a = a.lower()
            validation_datatype = True
            for i in options:
                if a == i:
                    validation_option = True
                    break
                else:
                    validation_option = False
        if validation_datatype == False:
            print("Not a valid datatype for input.")
        elif validation_option == False:
            print("Not a valid option.")
            print()
        else:
            break

    return a


def checker(data_type: str, text: str):
    breaker: bool
    while True:
        breaker = False
        a = input(text)

        if data_type == "int":
            try:
                a = int(a)
                breaker = True
                break
            except:
                ValueError
                print("Not a valid input (not int)")
        elif data_type == "str":
            a.lower()
            breaker = True
            break

        if breaker == True:
            break
    return a


"""
def checker_2_options(option1, option2, data_type: str):

    while True:
        breaker: bool = False
        validation_datatype: bool
        validation_option: bool

        a = input(">>> ")

        if data_type == "int":
            try:
                a = int(a)
                validation_datatype = True
                if (a == option1) or (a == option2):
                    #print("es correcto el tipo de variable (int)")
                    validation_option = True
                else:
                    #print("es incorrecto (int)")
                    validation_option = False
            except:
                ValueError
                #print("input no es int")
                validation_datatype = False
        elif data_type == "str":
            a = a.lower()
            validation_datatype = True
            if (a == option1) or (a == option2):
                #print("es correcto el tipo de variable(str)")
                validation_option = True
            else:
                #print("es incorrecto (str)")
                validation_option = False

        # (cumple con el tipo de dato?, cumple con las ociones?, elemento analizado)

        if validation_datatype == False:
            print("not correct data type")
        elif validation_option == False:
            print("not an option")
        else:
            break

    return a
"""
