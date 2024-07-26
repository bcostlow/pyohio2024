from dis import dis

a = b = 3
print(a)
print(b)
print("\n")

grp = a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)
print(grp)
print("\n")

def my_gen():
    for n in range(3):
        yield n*n


grp = a, b, c = my_gen()
print(a)
print(b)
print(c)
print(grp)
print("\n")

dis('a = 3')
print("\n")

dis('a = b = 3')
print("\n")

dis('grp = (a, b, c) = my_gen()')