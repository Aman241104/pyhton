class students:
    def fname(self):
        data=[]
        data.append((input(f"Enter First name:")))
        data.append((input(f"Enter last name:")))
        data.append(int(input(f"Enter Roll number:")))
        data.append(int(input(f"Enter age:")))
        data.append((input(f"Enter class:")))
        return data

    def report():
        marks=[]
        

stu1=students()
a=stu1.fname()
print(a)