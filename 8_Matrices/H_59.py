
def crear_lista(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return lst


n = 0
t = 3
a = t**2

lista = crear_lista(a)

temp_list = []
temp_list = [temp_list]*t

print(lista)

for i in range(1, t+1):
    temp_list[n].append(lista[lista.index(i)])


print(temp_list)
