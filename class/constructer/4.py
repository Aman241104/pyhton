# Write a program to create a class Car with attributes brand, model, and year, and a method to display the car's details

class car:
    def __init__(self):
        self.brand=""
        self.model=""
        self.year=0

    def getdata(self):
        self.brand=input("Enter cars's Brand:")
        self.model=input("Enter cars's model:")
        self.year=int(input("Enter cars's year:"))

    def display(self):  
            print(f"Brand: {self.brand}")
            print(f"Model: {self.model}")
            print(f"Year: {self.year}")
       

car1=car()
car1.getdata()
car1.display()