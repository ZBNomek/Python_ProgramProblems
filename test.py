
a = [[1, 2], [1, 2]]

b = [x for x in a]


print(a is b)
del a[-1]

print(a)
print(b)

print(a is b)
