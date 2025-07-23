dict={}
n=int(input("Enter number of data:"))
for i in range(0,n):
    x=input(f"Enter {i} Key:")
    y=input(f"Enter {i} value:")
    dict[x]=y

for key,value in dict.items():
    print(key+" : ",value)