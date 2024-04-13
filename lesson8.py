def apply_diff(setto, dic):




target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)  # => {'c', 'b'}