# 7. Determinar si un n´umero es primo.

def primo(numero: int) -> bool:
    prime: bool = True
    if numero <= 1:  # <-- El numero 1, 0 y los negativos no pueden ser primos
        prime = False
    else:
        if numero == 2:  # <-- el 2 genera conflicto con mi metodo pr lo que lo descarto por aparte
            pass
        else:
            for i in range(2, numero):
                if (numero % i) == 0:
                    prime = False
                    break

    return prime


"""
numero_primo: int = 23
numero_no_primo: int = 21
print(primo(numero_primo))
print(primo(numero_no_primo))
"""
