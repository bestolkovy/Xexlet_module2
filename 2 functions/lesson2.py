# Туточки мы вхуяриваем неопределенное количество имен, но не менее одного
# А на выходе нам прилетает приветствие всех Челиков.

def greet(name, *args):
    zhopa = ' and '.join((name, ) + args)
    return f'Hello, {zhopa}!'


print(greet('cc', 'rr', 'ss'))
