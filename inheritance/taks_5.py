# Problem: Define an Appliance class. Derive WashingMachine and Refrigerator classes with unique features.
# Problem: Build a base class Appliance, derive Computer to add processing speed, and further derive Laptop to include battery life.


class WashingMachine:
    def clean_cloths(self):
        print("*cleaning cloth Rrrrrrrrrrrrrrr*")

class Refrigerator:
    def cold(self):
        print("*Random frige noises*")

class Computer:
    def speed(self):
        self.speed=float(input("Enter Proceesing speed:"))
        print("speed: ",x,"GHz")

class laptop(Computer):
    def battery(self):
        self.batt=float(input("Enter Battery life: "))
        print("Battery life: ",y,"Mah")

class Appliance(WashingMachine,Refrigerator,laptop,Computer):
    print("")


app = Appliance()
app.clean_cloths()
app.cold()
app.speed()
app.battery()