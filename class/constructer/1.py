class Ex:
    def __init__(self, a, b):
        self.a = a  
        self.b = b
        print(f"a: {self.a}")
        print(f"b: {self.b}")

    def add(self):  
        print(f"Add: {self.a + self.b}")

    def sub(self):  
        print(f"Sub: {self.a - self.b}")



ex1 = Ex(10, 20)
ex1.add()  
ex1.sub()  
