# 2. Si 1/3 de las aves que hay en la granja son gallinas, y la mitad de las gallinas ponen 1 huevo
# cada 3 d´ıas y la otra mitad 1 huevo cada 5 d´ıas, ¿en un mes cu´antos huevos producen?
# (1 mes ≡ 30 d´ıas).

a = int  # numero de aves en la granja
huevos = int  # huevos producidos en el mes


def huevos_x_mes(a) -> float:
    grupo1: float = (a/6)*(30/3)
    grupo1 += (a/6)*(30/5)

    return grupo1


a = 60
huevos = huevos_x_mes(a)
print(huevos)
