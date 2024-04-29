def get_first_name(name_surname):
    first_name = ''
    for char in name_surname:
        if char != '_':
            first_name = first_name + char
        else:
            return first_name


def sort_by(key_func, user_list):
    sorted_list = sorted(user_list, key=key_func)
    return sorted_list


def get_unique(*args):
    result = set()
    for data in args:
        print(data)
        result |= set(data)
        print(result)
    return [*result]
