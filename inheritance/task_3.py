# Problem: Create a base class Person with name, derive Employee to add salary, and further derive Manager to add team size.

class Employee:
    def __init__(self):
        self.ename=""
        self.salary=0
    
    def sal(self):
        self.ename=input("Enter Employee name: ")
        self.salary = int(input("Enter Employee salary:"))

class Manager:
    def __init__(self):
        self.mname=""
        self.member=0
    
    def memeber(self):
        self.mname=input("Enter Manager name: ")
        self.member = int(input("Enter Total Team Members:"))


class person(Employee,Manager):
    def display(self):
        print("-------Details--------")
        print("Employee name: ",self.ename)
        print("Employee Salary: ",self.salary)
        print("Manager name: ",self.mname)
        print("Total team members: ",self.member)

p1= person()
p1.sal()
p1.memeber()
p1.display()
