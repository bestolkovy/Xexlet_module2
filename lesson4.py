def collect_indexes(content):
    dic = {}
    for index, volume in enumerate(content):
        dic.setdefault(volume, []).append(index)
    return dic


collect_indexes('hellodadoooh')
