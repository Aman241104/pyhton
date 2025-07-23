class maths:
    def add(self,a,b):
        print(f"Add: {a+b}")
    def sub(self,a,b):
        print(f"sub: {a-b}")

a=int(input("Enter first number: "))
b=int(input("Enter Second number: "))
print("Enter 1 for addition.")
print("Enter 2 for subtraction.")
ch=int(input("Enter choice: "))
obj = maths()

if(ch == 1):
    obj.add(a,b)
elif(ch == 2):
    obj.sub(a,b)
else:
    print("Enter Valid Choice.")
