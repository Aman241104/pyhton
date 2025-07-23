a = int(input("Enter: "))
b = int(input("Enter: "))
c = int(input("Enter: "))

match a,b,c:
    case _ if a==b==c:
        print("Equilateral triangle")
    case _ if a==b | b==c | c==a:
        print("Isosceles triangle") 
    case _ if 