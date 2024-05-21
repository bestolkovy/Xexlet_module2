def each2d(test, matrix):
    for i in (test(elem) for sublist in matrix for elem in sublist):
        if not i:
            return False
    return True


def some2d(test, matrix):
    for i in (test(elem) for sublist in matrix for elem in sublist):
        if i:
            return True
    return False


def sum2d(test, matrix):
    return sum(elem for sublist in matrix for elem in sublist if test(elem))
