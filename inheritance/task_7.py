# Create a class system that represents different kinds of employees in an organization. An employee could be both a Manager and a Developer, and you need to inherit both the managerial and technical skills.

class Manager:
    def mageing(self):
        print(self.emp," is *Doing the managerial stuffs.*")

class tech:
    def tech(self):
        print(self.emp," is *Doing Technical stuffs*")

class employee(Manager,tech):
    def empl(self):
        self.emp=input("Enter Employee name: ")

e1=employee()
e1.empl()
e1.mageing()
e1.tech()