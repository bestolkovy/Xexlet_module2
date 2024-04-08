def count_all(listva):
    listva = list(listva)
    dictionary = {}
    # listva = ('huy', 1, 34, 'mars', 'huy', 'mars')
    for i in listva:
        dictionary[i] = listva.count(i)
    return dictionary


print (count_all('*' * 20))
