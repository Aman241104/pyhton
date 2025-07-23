set1={11,22,33,44,55,"xyz",9.5}
set2={44,88,55,33,99,"xy",10.5,"xyz"}
print(set1)
print(set2)

set1.add("xy")
set1.remove(11)
print(set1)
print(set2)

union = set1 | set2
print(union)

intersaction = set1 & set2
print(intersaction)

dif = set1 ^ set2
print(dif)

diff = set1 - set2
print(diff)

diff2 = set2 - set1
print(diff2)