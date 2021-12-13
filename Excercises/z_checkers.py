"""
Esta parte son funciones que sirven para filtrar informacion de los 
inputs para que desta manera no hayan errores y muestren el el terminar
al usuario el error de su input, repitiendo esto hata que el usuario
ingrese un input valido y sirve con datos tipo str y  int, pero pueden
ser ampliados a más.
"""


# verifica que el input sea una de las opciones (filtro de dos opciones ej: a o b | si o no) ---> options = opciones posibles | datatype = el tipo de dato de las opciones y del input que se busca
def checker_options(options: tuple, data_type: str):
    while True:
        validation_datatype: bool
        validation_option: bool

        input_user = input(">>> ")
        print()

        if data_type == "int":
            try:
                input_user = int(input_user)
                validation_datatype = True
                for i in options:
                    if input_user == i:
                        validation_option = True
                        break
                    else:
                        validation_option = False
            except:
                ValueError
                validation_datatype = False
        elif data_type == "str":
            input_user = input_user.lower()
            validation_datatype = True
            for i in options:
                if input_user == i:
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

    return input_user

# verifica que el input sea el tipo de dato bucado ---> data_type = tipo de dato que se necesita | taxt = dato a analizar (sirve para ins, str y se puede adaptar a máss)


def checker(data_type: str, text: str):
    breaker: bool
    while True:
        breaker = False
        input_user = input(text)

        if data_type == "int":
            try:
                input_user = int(input_user)
                breaker = True
                break
            except:
                ValueError
                print("Not a valid input (not int)")
        elif data_type == "str":
            input_user.lower()
            breaker = True
            break

        if breaker == True:
            break
    return input_user


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
