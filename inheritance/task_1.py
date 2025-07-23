# Create a system where an animal can be both a Mammal and a Bird. Each class defines a method for making a sound, and the animal should inherit both sounds.

class mammal:
    def mammalsound(self):
        print("*mammal voices here*")

class bird:
    def birdsound(self):
        print("*Bird voices here*")

class animal(mammal,bird):
    print("")

objanimal = animal()
objanimal.birdsound()
objanimal.mammalsound()
