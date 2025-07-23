def crc(r,sw):
    if(sw==1):
        print("Area:",(4*3.14*r*r))
    elif(sw==2):
        print("Volume:",((4/3)*3.14*r*r*r))
    else:
        print("Enter Valid Choice")

r=int(input("Enter radius of the speare:"))
sw=int(input("For Area Enter 1/For volume Enter 2:"))

crc(r,sw)
