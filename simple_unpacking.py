
def demo():
    return "spam", "eggs"


# Demo "multiple return" is actually unpacking a tuple.
breakfast, second_breakfast = demo()
tasty_treats = demo()

print(breakfast)
print(second_breakfast)
print(tasty_treats)
print(type(tasty_treats))