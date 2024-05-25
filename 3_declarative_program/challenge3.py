# BEGIN
def product(sequence, *args):
    subproducts = product(*args) if args else [()]
    # ^ произведение оставшихся последовательностей вычисляем заранее
    # чтобы не строить заново для каждого элемента первой последовательности
    return [
        (first,) + subproduct
        for first in sequence
        for subproduct in subproducts
    ]
# END

# Примеры использования:
#print(product([1, 2], 'abc'))
# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]

#print(product('hello', [], 'world'))
# []



a = [1, 2]
b = 'abc'
c = [35, 36]
print(product(a, b ,c))