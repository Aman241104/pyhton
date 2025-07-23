# lst=[]
# for i in range(0,5):
#     lst.append(input())

# print("BEFORE")
# print(lst)

# n=int(input("How many number you want to enter:"))
# for i in range(0,n):
#     a=int(input("enter the index:"))
#     b=int(input("enter the value:"))
#     lst.insert(a,b)

# print("AFTER")
# print(lst)


lst=[]
for i in range(0,5):
    lst.append(input())

print("BEFORE")
print(lst)
a=int(input("enter the index:"))
b=int(input("enter the value:"))

if(a>5):
    print("enter valid index")

lst[i] = b

print("AFTER")
print(lst)