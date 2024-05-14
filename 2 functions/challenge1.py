def same_parity_filter(listik):
    if not listik:
        return []
    first = listik[0]
    filtered = filter(lambda x: x % 2 == first % 2, listik)
    return list(filtered)
