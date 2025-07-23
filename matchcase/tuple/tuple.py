t = (11,22,33)
print(t)

t1=((11,22),(2,1))
print(t1[0][1])
print(t1[1][0])

a=(1,2,3,4)
n=len(a)
for i in range(0,n):
    print(a[i])

lst=list(a)
n=len(lst)
lst.append(2)
lst.insert(2,20)
for i in range(0,n):
    print(lst[i])

x=tuple(lst)
print(x)
print(lst)