# 19. Si en la UN están podando árboles y cada rama tiene P hojas, y a cada árbol le quitaron K
# ramas, cuántos árboles se deben podar para obtener T hojas?.

"""
p = hojas x rama
k = ramas por arbol
t = hojas que se buscan

"""


def hojasxarbol(p: int, k: int, t: int) -> float:
    a = t/(p*k)
    return a


"""
hojas_x_rama: int = 6
ramas_x_arbol: int = 5
hojas: int = 75


print(hojasxarbol(hojas_x_rama, ramas_x_arbol, hojas), "Arboles")
"""
