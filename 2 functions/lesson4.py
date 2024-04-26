def updated(dict, **kwargs):
    new_dict = dict.copy()
    new_dict.update(kwargs)
    return new_dict
