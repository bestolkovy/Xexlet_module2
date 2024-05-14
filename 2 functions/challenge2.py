def compose(func1, func2):
    def inner(x):
        return func1(func2(x))
    return inner


# примеры функций на вход
def add5(x):
    return x + 5


def mul3(x):
    return x * 3


print(compose(mul3, add5)(1))
