# 80. Desarrollar un algoritmo que decodifique una cadena de caracteres mediante una cadena de
# correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
# car´acter el car´acter equivalente para el car´acter ‘a’, el segundo car´acter para la ‘b’y as´ı
# sucesivamente hasta la ‘z’. No se tiene traducci´on para las may´usculas ni para la ‘~n’.


def descodificador(cadena_codificada, cadena_correspondecias):
    cadena_correspondencias: tuple = (
        cadena_correspondecias, "abcdefghijklmnopqrstuvwxyz")
    cadena_descodificada = ""
    for i in cadena_codificada:
        try:
            index = cadena_correspondencias[0].index(str(i))
            cadena_descodificada += cadena_correspondencias[1][index]
        except:
            ValueError
            cadena_descodificada += " "

    return cadena_descodificada


cadena: str = "qs lxk rt egsgdwoq"
cadena_correspondencias: str = "qwertyuiopasdfghjklzxcvbnm"

print(descodificador(cadena, cadena_correspondencias))
