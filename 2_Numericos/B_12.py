# 12. Dados los coeficientes de un polinomio de grado dos y un n´umero real, evaluar la derivada del
# polinomio en ese n´umero.


# Ej : 2x^2 + 3x

termino_grado_2: int = 2  # 2x^2
termino_grado_1: int = 3  # 3x
x: int = 3


def derivada_resulta(a, b, x):
    return(2*a*x)+(1*b)


print(">", derivada_resulta(termino_grado_2, termino_grado_1, x))
