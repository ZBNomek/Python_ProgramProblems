# 4. Al granjero se le da˜no el corral y no sabe si volver a cercar el corral con madera, alambre de
# p´uas o poner reja de metal. Si va a cercar con madera debe poner 4 hileras de tablas, con
# varilla 8 hileras y con alambre solo 5 hileras, ´el quiere saber que es lo menos costoso para
# cercar si sabe que el alambre de p´uas vale P por metro, las tablas a Q por metro y las varillas
# S por metro. Dado el tama˜no del corral y los precios de los elementos, ¿cu´al cerramiento es
# el m´as econ´omico?.

# Precios material

p: int = 10    # precio alambre por metro
q: int = 12    # precio madera por metro
s: int = 8     # precio varilla por metro
m: int = 5     # medida m del corral
n: int = 6     # medida n del corral


def material_barato(p, q, s, m, n) -> str:
    precio_puas: int = 10 * p * (n+m)
    precio_madera: int = 8 * q * (n+m)
    precio_varilla: int = 16 * s * (n+m)

    if (precio_puas <= precio_madera) and (precio_puas <= precio_varilla):
        return "Alambre de Puas"
    elif(precio_varilla <= precio_madera) and (precio_varilla <= precio_madera):
        return "Varilla"
    else:
        return "Tablas de madera"


print(material_barato(p, q, s, m, n))
