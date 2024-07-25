print(list(range(5)))

print("\nfirst, *rest = range(5)")
first, *rest = range(5)
print(first)
print(rest)

print("\nfirst, *middle, last = range(5)")
first, *middle, last = range(5)
print(first)
print(middle)
print(last)

print("\nfirst, second, *last = range(5)")
first, second, *last = range(5)
print(first)
print(second)
print(last)

print("\nfirst, second, *extra, last = range(5)")
first, second, *extra, last = range(5)
print(first)
print(second)
print(extra)
print(last)

# extras

# kind of silly, but...
print("\nfirst, second, third, *fourth, last = range(5)")
first, second, third, *fourth, last = range(5)
print(first)
print(second)
print(third)
print(fourth)
print(last)

# By convention, use _ for values you don't care about
print("\nfirst, *_, last = range(5)")
first, *_, last = range(5)
print(first)
print(last)

