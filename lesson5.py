def all_unique(content):
    listik = list(content)
    return len(listik) == len(set(listik))


print(all_unique(iter([1, 2, 3, 5])))
