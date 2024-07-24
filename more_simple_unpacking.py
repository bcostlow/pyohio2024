
def demo():
    return ['spam', 'eggs']


breakfast, second_breakfast = demo()
print(breakfast, second_breakfast)


def demo_with_dict():
    return {'spam': 1, 'eggs': 3}


breakfast, second_breakfast = demo_with_dict()
print(breakfast, second_breakfast)

first, second = demo_with_dict().items()
print(first, second)

first, second = range(2)
print(first, second)


def demo_gen():
    for number in range(3):
        yield number + 1


one, two, three = demo_gen()
print(one, two, three)