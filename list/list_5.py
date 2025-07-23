lst=[]
n=int(input("enter number of input:"))
for i in range(0,n):
    lst.append(int(input()))




c=0
while(c==0):
    print("Enter 1 for inserting any value at end")
    print("Enter 2 for inserting any value on given position")
    print("Enter 3 to remove any index")
    print("Enter 4 to remove any value")
    x=input("Enter operation:")
    
    if(x == '1'):
        lst.append(int(input("Enter value:")))
        print(lst)
    elif(x=='2'):
        i = int(input("Enter index:"))
        v = int(input("Enter value:"))
        lst.insert(i,v)
        print(lst)
    elif(x=='3'):
        i = int(input("Enter index:"))
        lst.pop(i)
        print(lst)
    elif(x=='4'):
        v = int(input("Enter value:"))
        lst.remove(v)
        print(lst)
    else:
        print("Enter valid operation")
    print('Enter 0 to operate again')
    c=int(input("Enter:"))

