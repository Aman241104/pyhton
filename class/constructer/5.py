# Problem: Multi-Tier Shopping Discount System
# A shopping platform offers different discount rules based on the total purchase amount, membership status, and time of purchase. The discount rules are as follows:
# 1. If the purchase amount is $500 or more:
#    - Members get a 20% discount.
#    - Non-members get a 10% discount.
# 2. If the purchase amount is between $200 and $499:
#    - Members get a 15% discount.
#    - Non-members get a 5% discount.
# 3. If the purchase amount is less than $200:
#    - Members get a 5% discount.
#    - Non-members get no discount
# 4. If the purchase is made during a sale event, both members and non-members get an additional 5% discount on top of their regular discount.
# Write a program to calculate the final price for the user. -->\

import random

class shopping:
    def __init__(self):
        self.user=""
        self.membership=0
        self.items=0
        self.amount=0
        self.discount=0

    def getdata(self):
        self.user=input("Enter Username:")

        flag = 0 
        while(flag == 0):
            self.membership=(input("Are you a member? Y/N"))
            if(self.membership == 'Y'):
                self.membership = 1
                flag=1
                break
            elif(self.membership == 'N'):
                self.membership = 0
                flag=1
                break
            else:
                print("Enter Valid Choice")
                break

        self.items=random.randint(0,15)
        self.amount=random.randint(5,700)
        print("----------Cart Details---------")
        print(f"Total items: {self.items}")
        print(f"Amount: {self.amount}")
        print(self.membership)

    def disc(self):
        if(self.membership == 1):
            if(self.amount>=500):
                self.discount=(self.amount * 20)/100
            elif(self.amount>=200 and self.amount<=499):
                self.discount=(self.amount * 15)/100 
            elif(self.amount<200):
                self.discount=(self.amount * 5)/100

        elif(self.membership == 0):
            if(self.amount>=500):
                self.discount=(self.amount * 10)/100
            elif(self.amount>=200 and self.amount<=499):
                self.discount=(self.amount * 5)/100
            elif(self.amount<200):
                self.discount=0
            
    def display(self):
        print("----------Cart Details---------")
        print(f"Total items: {self.items}")
        print(f"Amount: {self.amount}")

        if(self.membership == 1):
            print(f"You are a member.")
        elif(self.membership == 0):
            print(f"You are not a member.")
            
        print(f"Discount: {self.discount}")
        print(f"Total Amount: {self.amount - self.discount}")


cart1=shopping()
cart1.getdata()
cart1.disc()
cart1.display()