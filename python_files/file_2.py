with open('even.txt','w') as even:
    even.close()

with open('odd.txt','w') as odd:
    odd.close()

n=int(input("How many number wanted to enter: "))
for i in range(0,n):
    num=int(input("Enter Number: "))
    if(num%2 == 0):
        with open('even.txt','a') as even:
            even.write(f"{num}, ")
            even.close()
    else:
        with open('odd.txt','a') as odd:
            odd.write(f"{num}, ")
            odd.close()
