def filter_map(func, itterator):
    mutilated_list = []
    for index in itterator:
        if func(index)[0] is True:
            mutilated_list.append(func(index)[1])
    return mutilated_list
