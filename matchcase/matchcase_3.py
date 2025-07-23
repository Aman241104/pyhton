per = int(input("Enter: "))

match per:
    case _ if 90<per:
        print("A Grade")
    case _ if 80<per>=90:
        print("B Grade")
    case _ if 70<per>=80:
        print("C Grade")
    case _ if 60<per>=70:
        print("D Grade")
    case _ if 60<per>=40:
        print("E Grade")
    case _ if per<=40:
        print("F Grade")
    case _:
        print("Not Valid")



# match per:
#     case _ if(per>=90):
#         print("A Grade")
#     case _ if(per>80 and per<=90):
#         print("B Grade")
#     case _ if(per>70 and per<=80):
#         print("C Grade")
#     case _ if(per>=60 and per<=70):
#         print("D Grade")
#     case _ if(per>40 and per<=60):
#         print("E Grade")
#     case _ if(per<=40):
#         print("F Grade")
#     case _:
#         print("Not Valid")