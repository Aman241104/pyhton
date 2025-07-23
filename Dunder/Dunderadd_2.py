class addition:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def prtSum(self):
        print("SUM of a: ",self.a)
        print("SUM of b: ",self.b)

        
    def __add__(self,nu):
        sum_a = self.a + nu.a
        sum_b = self.b + nu.b
        print("Num a1:",self.a)
        print("Num a2:",nu.a)
        print("Num b1:",self.b)
        print("Num b2:",nu.b)
        return addition(sum_a,sum_b)
    
n1 = addition(30,20)
n2 = addition(40,10)
sum = n1 + n2
sum.prtSum()