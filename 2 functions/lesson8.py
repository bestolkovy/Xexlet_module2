from functools import reduce
import operator


def keep_truthful(iterium):
    return filter(operator.truth, iterium)


def sum_abs(iterium):
    return sum(list(map(abs, iterium)))


def walk(dictionary, path):
    # Используем reduce для последовательного получения значений по пути
    return reduce(operator.getitem, path, dictionary)
