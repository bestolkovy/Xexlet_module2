def make_user(name_value, age_value):
    dictionary = {'name': name_value,
                  'age': age_value}
    return dictionary


def format_user(huy):
    string = f"{huy['name']}, {huy['age']}"
    return string


pavel = make_user('Pidor', 19)
print(pavel)

d = format_user(pavel)
print(d)
