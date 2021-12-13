# 17. Dado el radio de un c´ırculo, calcular el ´area y per´ımetro del cuadrado, pent´agono y hex´agono
# adentro (inscrito en un c´ırculo) y afuera (inscribiendo al c´ırculo).

import math


def perimetro_ext(radio: float, lados: int) -> float:
    angle: float = 360/(2*lados)
    angle = (angle*math.pi)/180
    perimetro: float = (lados*2) * (radio * (math.tan(angle)))
    return perimetro


def area_ext(radio: float, lados: int) -> float:
    area: float = ((perimetro_ext(radio, lados))*radio)/2
    return area


def perimetro_int(radio: float, lados: int) -> float:
    angulo: float = 360/(2*lados)
    angulo = (angulo*math.pi)/180
    perimetro: float = (lados*2) * (radio * (math.sin(angulo)))
    return perimetro


def area_int(radio: float, lados: int) -> float:
    angulo: float = 360/(2*lados)
    angulo = (angulo*math.pi)/180
    area: float = ((perimetro_int(radio, lados)) *
                   (radio * (math.cos(angulo))))/2
    return area


def funcion_display_C17(r: float, formas: list) -> None:

    print("-----------------------------------------------------------------")
    print()
    print("El radio del circulo dado es de ", r)

    for i in formas:
        print("Ejercicions con un ", i[0])
        print()
        print("Perimetro de un ", i[0], " inscribiendo a una circunferencia:")
        print(perimetro_ext(r, i[1]))
        print()
        print("Area de un ", i[0], " inscribiendo a una circunferencia:")
        print(area_ext(r, i[1]))
        print()
        print("Perimetro de un ", i[0], " inscrito en una circunferencia:")
        print(perimetro_int(r, i[1]))
        print()
        print("Area de un ", i[0], " inscrito en una circunferencia:")
        print(area_int(r, i[1]))
        print()
        print("-----------------------------------------------------------------")
        print()


"""
radio = 8
formas = [("cuadrado", 4), ("pentagono", 5), ("hexagono", 5)]
funcion_display_C17(radio, formas)
"""

"""

---> Programa antes de simplicarlo que me dio pesar borrar :) <---

# cuadrado:

def area_cuadrado_ext(r: int):
    a: float = 4 * pow(r, 2)
    return a


print()
print("area cuadrado externo -> good")
print(area_cuadrado_ext(r))


def perimetro_cuadrado_ext(r: int):
    a: float = 8*r
    return a


print()
print("perimetro cuadrado externo -> good")
print(perimetro_cuadrado_ext(r))


def area_cuadrado_int(r: int):
    a: float = 2 * pow(r, 2)
    return a


print()
print("area cuadrado interno -> good ")
print(area_cuadrado_int(r))


def perimetro_cuadrado_int(r: int):
    a: float = 4 * r * math.sqrt(2)
    return a


print()
print("perimetro cuadrado interno -> good ")
print(perimetro_cuadrado_int(r))

# Pentágono


def perimetro_pentagono_ext(r: int):
    p: float = (2 * r * math.tan((36*math.pi)/180))*5
    return p


print()
print("perimetro pentagono externo-> good ")
print(perimetro_pentagono_ext(r))
print()


def area_pentagono_ext(r: int):
    a: float = (perimetro_pentagono_ext(r)*r)/2
    return a


print("area pentagono externo-> good ")
print(area_pentagono_ext(r))
print()


def perimetro_pentagono_int(r: int):
    p: float = 10*(r * math.sin((36*math.pi)/180))
    return p


print("perimetro pentagono interno-> good ")
print(perimetro_pentagono_int(r))
print()


def area_pentagono_int(r: int):
    a: float = (perimetro_pentagono_int(r) * 8*(math.cos((36*math.pi)/180)))/2
    return a


print("area pentagono interno-> good ")
print(area_pentagono_int(r))
print()

# Hexágono


def perimetro_hexagono_ext(r: int):
    p: float = 12 * (8 * math.tan((30*math.pi)/180))
    return p


print("perimetro hexagono externo-> good ")
print(perimetro_hexagono_ext(r))
print()


def area_hexagono_ext(r: int):
    a: float = ((perimetro_hexagono_ext(r))*r)/2
    return a


print("area hexagono externo-> good ")
print(area_hexagono_ext(r))
print()


def perimetro_hexagono_int(r: int):
    p: float = 12 * (r * math.sin((30*math.pi)/180))
    return p


print("perimetro hexagono interno-> good ")
print(perimetro_hexagono_int(r))
print()


def area_hexagono_int(r: int):
    a: float = ((perimetro_hexagono_int(r)) *
                (r * (math.cos((30*math.pi)/180)))/2)
    return a


print("area hexagono interno-> good ")
print(area_hexagono_int(r))
print()
"""
