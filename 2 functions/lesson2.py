def greet(name, *args):
    q = (name, )
    zhopa = ' and '.join((name, ) + args)
    return f'Hello, {zhopa}!'


print(greet('cc', 'rr', 'ss'))
