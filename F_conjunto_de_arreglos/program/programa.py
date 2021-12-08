#from compilation_defs import union_conjuntos, interseccion_conjuntos, diferencia_conjuntos, diferencia_sim_conjuntos, pertenencia, contenido
import compilation_defs as comp

A: list = [*range(1, 11)]
B: list = [*range(5, 21)]
x1: int = 2
x2: int = 15


AuB: list = comp.union_conjuntos(A, B)
AnB: list = comp.interseccion_conjuntos(A, B)
A_B: list = comp.diferencia_conjuntos(A, B)
B_A: list = comp.diferencia_conjuntos(B, A)
A_sim_B: list = comp.diferencia_sim_conjuntos(A, B)
x1EA: list = comp.pertenencia(x1, A, B)
x2EA: list = comp.pertenencia(x1, A, B)
AcB: bool = comp.contenido(A, B)
BcA: bool = comp.contenido(B, A)

print(A)
print(B)
print()
print("UNION:")
print(AuB)
print()
print("INTERSECCION:")
print(AnB)
print()
print("DIFERENCIA:")
print(A_B)
print(B_A)
print()
print("DIFERENCIA SIMETRICA:")
print("PERTENECE A:")
print(x1, "E A? / E B?")
print(x1EA)
print()
print(x2, "E A? / E B?")
print(x2EA)
print()
print("CONTIENE:")
print("A C B?")
print(AcB)
print()
print("B C A?")
print(BcA)
print()
