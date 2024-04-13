def toggle(flag, setto):
    if flag in setto:
        setto.discard(flag)
    else:
        setto.add(flag)


def toggled(flag, setto):
    setto1 = setto.copy()
    if flag in setto:
        setto1.discard(flag)
        return setto1

    else:
        setto1.add(flag)
        return setto1
