# 3. Si los escorpiones de la granja se venden a China, y hay escorpiones de tres diferentes tama˜nos:
# peque˜nos (con un peso de 20 gramos), medianos (con un peso 30 gramos) y grandes (con
# un peso de 50 gramos), ¿cu´antos kilos de escorpiones se pueden vender sin que decrezca la
# poblaci´on a menos de 2/3?.

p: int  # escorpiones pequeños
m: int  # escprpiones medianos
g: int  # escorpiones grandes


def kilos(p, m, g) -> float:
    return ((p*20)+(m*30)+(g*50))/3000


venta_kilos: float = kilos(10, 15, 5)

print(venta_kilos)
