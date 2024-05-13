def memorized(func):
    dicto = {}

    def wrapper(arg):
        if dicto.get(arg) is None:
            dicto[arg] = func(arg)
        return dicto[arg]

    return wrapper
