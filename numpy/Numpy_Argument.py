import numpy as np

three = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

# print(three.argmax())
# return index number
# print(three.argmin())
# print(three.argmax(axis=1))
print(three.argmax(axis=0))

# axis=0 : check column-wise (top to bottom)

# axis=1 : check row-wise (left to right)