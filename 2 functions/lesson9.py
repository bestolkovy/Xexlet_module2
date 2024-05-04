def greet(name, surname):
    return f'Hello, {name} {surname}!'


# решение
def partial_apply(func, name):
    def inner(surname):
        return func(name, surname)
    return inner


def flip(func):
    def inner(name, surname):
        return func(surname, name)
    return inner


# исполнение
f = partial_apply(greet, 'Dorian')
print(f('Grey'))

s = flip(greet)
print(s('huy', 'pizda'))