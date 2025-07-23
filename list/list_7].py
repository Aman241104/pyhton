n=int(input("enter number of input for both list:"))

l1=[]
l2=[]

for i in range(0,n):
    l1.append(int(input(f"Enter for list 1 index {i}:")))

for i in range(0,n):
    l2.append(int(input(f"Enter for list 2 index {i}:")))

for i in range(0,n):
    l2[i] = (l2[i] + l1[i])

print(l2)