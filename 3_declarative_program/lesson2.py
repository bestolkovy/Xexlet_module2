def keep_odds_from_odds(listok):
    if type(listok) is list:
        listok[:] = [x for i, x in enumerate(listok) if i % 2 == 0]
        for i in range(len(listok)):
            keep_odds_from_odds(listok[i])


def odds_from_odds(listok):
    if isinstance(listok, list):
        return [odds_from_odds(sublist) for i, sublist in enumerate(listok) if i % 2 == 0]
    else:
        return listok

l = [
            [1, 2, 3, 4, 5],
            ['c', 'a', 't'],
            ['d', 'o', 'g'],
            [100, 200, 300, 400],
            [True, False],
            [],
            [],
        ]


keep_odds_from_odds(l)
print(l)
 #a = odds_from_odds(l)
#print(a)
#print(l)
