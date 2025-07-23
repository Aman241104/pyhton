import numpy as np;

# a = np.array([10,20,30,40,50])
# print("array: ",a)
# print("array * 5: ",a*5)
# print("sum: ",np.sum(a))
# print("mean: ",np.mean(a))
# print("min: ",np.min(a))
# print("max: ",np.max(a))

# print("random.rand(5)*10: ",np.random.rand(5)*10)
# print("random.ranint(5): ",np.random.randint(5))

# print("arrange from 1 to 10: ",np.arange(1,10))
# print("arrange from 1 to 10 with gap of 2: ",np.arange(0,10,2))


# a = np.array([11,22,33,44,55])
a = np.array([[11,22],[33,44]])
# a = np.array([[[11,22,33],[44,55,66]],[[11,22,33],[44,55,66]],[[11,22,33],[44,55,66]]])

print(type(a))
print("Size : ",a.size)
print("Shape : ",a.shape)
print("Dimention : ",a.ndim)
print("ItemSize : ",a.itemsize)
print("Type : ",a.astype(int))
print("Type : ",a.astype(float))
print("Type : ",a.astype(str))