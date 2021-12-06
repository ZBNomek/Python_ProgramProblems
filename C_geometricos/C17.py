import math
r = 8


def perimetro_ext(r: int, l: int):
    angle: float = 360/(2*l)
    angle = (angle*math.pi)/180
    p: float = (l*2) * (r * (math.tan(angle)))
    return p


def area_ext(r: int, l: int):
    a: float = ((perimetro_ext(r, l))*r)/2
    return a


def perimetro_int(r: int, l: int):
    angle: float = 360/(2*l)
    angle = (angle*math.pi)/180
    p: float = (l*2) * (r * (math.sin(angle)))
    return p


def area_int(r: int, l: int):
    angulo: float = 360/(2*l)
    angulo = (angulo*math.pi)/180
    a: float = ((perimetro_int(r, l))*(r * (math.cos(angulo))))/2
    return a


formas = [("cuadrado", 4), ("pentagono", 5), ("hexagono", 5)]
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
