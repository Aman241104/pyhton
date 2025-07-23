num=[0,-10,-20,-30,-40,-50,-60,70,50,40,60,20,22,-98,-95,-65]

def sum(args):
    count=0
    sum=0
    x=int(input("How many number you want to add:"))
    for i in args:
        if(i>=0 and count<= x):
            count=count+1
            sum=i+sum
    
    return sum


s=sum(num)
print(f"Total:{s}")