num=int(input("Enter number of inputs:"))
lst=[]
e=[]
avg=0
for i in range(0,num):
    x=int(input(f"Enter {i+1} number of inputs:"))
    lst.append(x)
    avg=avg+lst[i]
print("Enter 1 for positive numbers")
print("Enter 2 for Negative numbers")
print("Enter 3 for Odd numbers")
print("Enter 4 for Even numbers")
print("Enter 5 for Zero numbers")
print("Enter 6 for Average.")
sw=int(input("Enter choice:"))

if(sw == 1):
    for i in range(0,num):
        if(lst[i] > 0):
            e.append(lst[i])
    print("Positive:",e)
    
elif(sw == 2):
    for i in range(0,num):
        if(lst[i]<0):
            e.append(lst[i])
    print("Negaitive:",e)
    
        
elif(sw == 3):
    for i in range(0,num):
        if(lst[i]%2== 0):
            e.append(lst[i])
    print("Even:",e)
    
elif(sw == 4):
    for i in range(0,num):
        if(lst[i]%2 != 0):
            e.append(lst[i])
    print("Odd:",e)

elif(sw == 5):
    for i in range(0,num):
        if(lst[i]==0):
            e.append(lst[i])
    print("Zero:",e)
        
elif(sw == 6):
    print("Avg:",(avg/num))
    
else:
    print("Enter valid choice")
