def getData(**kwargv):
    print(kwargv)

getData(name = "amit",age = 22,city = "delhi",country = "india",x=100) 



def yzx(*args,name,**kwargv):
    print(f"args:{args}")
    print(f"name:{name}")
    print(f"kwargv:{kwargv}")
yzx(10,11,"abc","xyz",name="amit",age = 22,city = "delhi",country = "india",x=100)