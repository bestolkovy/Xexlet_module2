def length(listo):
    if listo == []:
        return 0
    _, *tail = listo
    return 1 + length(tail)


def reverse_range(begin, end):
    if end - begin == 0:
        return [end]
    else:
        return [end] + reverse_range(begin, end - 1)


def filter_positive(listo):
    if not listo:
        return []
    head, *tail = listo
    if head > 0:
        return [head] + filter_positive(tail)
    else:
        return filter_positive(tail)
