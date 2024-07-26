
def extra_args(first, second, *args):
    print(first, second, args)


extra_args('spam', 'eggs', 'sausage', 'strawberry tart')


def extra_kw(spam=1, eggs=3, **kwargs):
    print(spam, eggs, kwargs)


extra_kw(spam=2, sausage=5, tart_with_rat=1)