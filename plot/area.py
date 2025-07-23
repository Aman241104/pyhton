class shape:
    def area(x,y):
        area =  x*y;
        print(f"area(x*y): {area}")

class square(shape):
    def area(x,y):
        area = 1/2*x*y
        print(f"area(1/2*x*y): {area}")

class circle(shape):
    def area(x):
        area = 3.14*x*x; 
        print(f"area(pi*r^2): {area}")

obj1=square()
obj2=circle()
obj1=shape()

square.area(10,20)
circle.area(10)
shape.area(5,2)


    
