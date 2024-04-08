def count_all(items):
    counters = {}
    for item in items:
        print (item)
        counters[item] = counters.get(item, 0) + 1
        print(counters)
    return counters

count_all('heelohhhhh')