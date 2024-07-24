

order = {'spam': 1, 'eggs': 3}

# looping over items() produces a tuple
# that gets unpacked into key, value
for key, value in order.items():
    print(key, value)

# looping without unpacking the tuple
# proving it's a tuple
for item in order.items():
    print(item)



