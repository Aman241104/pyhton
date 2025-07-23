import numpy as np;

x=np.arange(1,10).reshape(3,3)
y=np.arange(1,10).reshape(3,3)

print(f"add: {x+y}")
print(f"add: {np.add(x,y)}")

print(f"sub: {x-y}")
print(f"sub: {np.subtract(x,y)}")

print(f"mul: {x*y}")
print(f"mul: {np.multiply(x,y)}")

print(f"div: {x/y}")
print(f"div: {np.divide(x,y)}")