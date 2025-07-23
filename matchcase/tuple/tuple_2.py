t1=(1,2,3,4,5)
n=len(list(t1))

for i in range(0,n):
    sum=sum+t1[i]

print(f"sum:{sum}")


t2=(5,4,3,2,1)
l1=list(t1)
l2=list(t2)
n=len(list(t1))

for i in range(0,n):
    l2[i] = l2[i] + l1[i]

t2=tuple(l2)
print(t2)