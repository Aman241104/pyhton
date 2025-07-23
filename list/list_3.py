lst=[]
n=int(input("enter number of input:"))
for i in range(0,n):
    lst.append(input())

print("BEFORE")
print(lst)
a=int(input("enter the index:"))
if(a>n):
    print("enter valid index")
b=int(input("enter the value:"))



lst[a] = b

print("AFTER")
print(lst)