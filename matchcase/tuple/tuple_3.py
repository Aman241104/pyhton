lst=[]
n=int(input("enter number of input:"))
for i in range(0,n):
    lst.append(int(input()))

tpl=tuple(lst)
print(tpl)

n=len(lst)
m1=0
for i in range(0,n):
    if(tpl[i] >= m1 ):
        m1=tpl[i]
print("first max:",m1)
lst.remove(m1)
# print(lst)
tpl=tuple(lst)
m1=0
for i in range(0,(n-1)):
    if(tpl[i] >= m1 ):
        m1=tpl[i]
print("second max:",m1)