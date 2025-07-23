
lst=[]
for i in range(0,5):
    lst.append(input())

n=len(lst)
max=lst[0]
for i in range(0,n):
    if(lst[i] >= max):
        max = lst[i]

print(f"max is {max}")


