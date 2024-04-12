def count_all(listva):
    listva = list(listva)
    dictionary = {}
    for i in listva:
        dictionary[i] = listva.count(i)
    return dictionary
