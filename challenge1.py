# скрэббл
from collections import Counter


def scrabble(string, word):
    str_dict = dict(Counter(string.upper()))
    word_dict = dict(Counter(word.upper()))
    for k in word_dict:
        if word_dict[k] > str_dict.get(k, 0):
            return False
    return True
