lst=[]
n=int(input("enter number of input:"))

for i in range(0,n):
    lst.append(int(input()))

co=0
a=int(input("Enter Which number to count:"))
for i in range(0,n):
    if(lst[i] == a):
        co=co+1

print(f"count:{co}")