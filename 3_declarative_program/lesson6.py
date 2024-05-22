def my_map(f, xs):
    for x in xs:
        yield f(x)


def my_filter(f, xf):
    for x in xf:
        if f(x):
            yield (x)


def replicate_each(n, xs):
    for x in xs:
        yield from (x for _ in range(n))


print(list(replicate_each(3, [1, 'a'])))
