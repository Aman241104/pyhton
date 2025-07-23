# Problem: Create a base class Animal with species attribute, a derived class Mammal with warm-blooded property, and a further derived class Dog with a bark method.

class animal:
    def animal(self):
        print("Animal Attributes here")

class mammal(animal):
    def mammal(self):
        print("Warn blooded")

class dog(mammal):
    def bark(self):
        print("*Random Dog Bark Noise*")

objdog = dog()
objdog.animal()
objdog.mammal()
objdog.bark()