import itertools


def length_frequencies(listo):
    sorted_listo = sorted(listo, key=len)
    grouped = itertools.groupby(sorted_listo, key=len)
    return {x: len(list(y)) for x, y in grouped}
