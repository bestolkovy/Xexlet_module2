def number_of_unique_letters(stringo):
    return len({x.upper() for x in stringo if x.isalpha()})
    

print(number_of_unique_letters("AaBbCcDd"))