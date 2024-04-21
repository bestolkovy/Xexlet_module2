from map import get_hash


def get_or_default(h_table, keyyo, empty_volume):
    index = get_hash(keyyo)
    if not h_table[index]:
        return empty_volume
    else:
        return h_table[index][1]
