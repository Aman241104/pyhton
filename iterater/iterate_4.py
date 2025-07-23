import itertools

a = [11,22,33,44,55]
b = [33,44,55,66,77,99]

for item in itertools.chain(a,b):
    print(item)