def is_prime(argument):
    for i in range(2, int(argument ** 0.5 + 1)):
        if argument % i == 0:
            return False
    return True


def say_prime_or_not(argument):
    if is_prime(argument):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return print(right_answer)


say_prime_or_not(10)
