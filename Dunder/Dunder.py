class addition:
    def __init__(self, n):
        self.n = n

    def prtSum(self):
        print("Value:", self.n)

    def __add__(self, ot):
        result = self.n + ot.n
        print("Addition:")
        print("Num 1:", self.n)
        print("Num 2:", ot.n)
        return addition(result)

    def __sub__(self, ot):
        result = self.n - ot.n
        print("Subtraction:")
        print("Num 1:", self.n)
        print("Num 2:", ot.n)
        return addition(result)

    def __mul__(self, ot):
        result = self.n * ot.n
        print("Multiplication:")
        print("Num 1:", self.n)
        print("Num 2:", ot.n)
        return addition(result)

    def __str__(self):
        return f"addition({self.n})"

    def __eq__(self, ot):
        return self.n == ot.n

    def __lt__(self, ot):
        return self.n < ot.n

    def __le__(self, ot):
        return self.n <= ot.n

    def __gt__(self, ot):
        return self.n > ot.n

    def __ge__(self, ot):
        return self.n >= ot.n

n1 = addition(30)
n2 = addition(40)

sum_result = n1 + n2
sum_result.prtSum()

sub_result = n2 - n1
sub_result.prtSum()

mul_result = n1 * n2
mul_result.prtSum()

print("String:", str(n1))
print("Equal:", n1 == n2)
print("Less Than:", n1 < n2)
print("Greater Than:", n1 > n2)
