def remove_first_level(listo):
    new_list = []
    for i in range(len(listo)):
        if not listo[i]:
            continue
        else:
            new_list += listo[i]
    return new_list
        
