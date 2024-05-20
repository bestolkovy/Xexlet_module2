def non_empty_truths(listok):
    return ([x for x in [[y for y in listik if y] for listik in listok] if x])
