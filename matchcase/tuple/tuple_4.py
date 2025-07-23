lst=[]
n=int(input("enter number of input:"))
for i in range(0,n):
    lst.append(int(input()))

n=len(lst)
even=[]
odd=[]
for i in range(0,n):
    if(lst[i]%2 == 0):
        even.append(lst[i])
    else:
        odd.append(lst[i])

et=tuple(even)
ot=tuple(odd)
print("even:",et)
print("odd:",ot)
