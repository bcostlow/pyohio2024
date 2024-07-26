
def three_args(one, two, three):
    print(one, two, three)


data = ['red', 'green', 'blue']
three_args(*data)
three_args(*range(3))


def key_args(color='red', size=10):
    print(color, size)


key_args()
shirt = {'color': 'blue', 'size': 12}
key_args(**shirt)



