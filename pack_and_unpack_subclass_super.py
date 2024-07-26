
class BreakFast:
    def __init__(self, spam, eggs, add_sausage=True):
        self.spam = spam
        self.eggs = eggs
        self.add_sausage = add_sausage


class SecondBreakfast(BreakFast):
    def __init__(self, *args, some_rat=True, **kwargs):
        self.some_rat = some_rat
        super(SecondBreakfast, self).__init__(
            *args,
            **kwargs
        )


second_breakfast = SecondBreakfast(1, 3, some_rat=False)

print(second_breakfast)
print(vars(second_breakfast))
