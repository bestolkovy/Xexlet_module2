d = {}
d.setdefault('a', d.setdefault('b', [])).append(1)
print (d)
