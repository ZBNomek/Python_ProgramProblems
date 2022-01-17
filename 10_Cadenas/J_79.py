# 79. Desarrollar un algoritmo que codifique una cadena de caracteres mediante una cadena de
# correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
# car´acter el car´acter equivalente para el car´acter ‘a’, el segundo car´acter para la ‘b’y
# as´ı sucesivamente hasta la ‘z’. No se tiene traducci´on para las may´usculas ni para la ‘~n’.

def codificador(cadena, cadena_correspondecias):
    cadena = cadena.lower()
    cadena_correspondencias: tuple = (
        cadena_correspondecias, "abcdefghijklmnopqrstuvwxyz")
    cadena_codificada = ""
    for i in cadena:
        try:
            index = cadena_correspondencias[1].index(str(i))
            cadena_codificada += cadena_correspondencias[0][index]
        except:
            ValueError
            cadena_codificada += " "

    return cadena_codificada


cadena: str = "al sur de colombia"
cadena_correspondencias: str = "qwertyuiopasdfghjklzxcvbnm"

print(codificador(cadena, cadena_correspondencias))
