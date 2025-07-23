def xyz(args,*argv):
    print(f"First: {args}")
    for i in argv:
        print(f"others: {i}")
xyz("ABC","x","y","z")



def yzx(*args,name):
    print(f"args:{args}")
    print(f"name:{name}")
yzx(10,11,"abc","xyz",name="aaaaa")

