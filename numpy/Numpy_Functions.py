import numpy as np

three = np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
                  [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]])
three = np.arange(1, 10, 3)
# print(three)

# three = np.linspace(1, 50, 4)
# print(three)

# three = np.arange(1, 10).reshape(3,3)
# print(three)

# ravel


array = np.arange(15).reshape(3, 5)
# print("Original : \n", array)

# print("\nravel() : ", array.ravel())
print("Reshaping array : ", np.ravel(array,order='f'))

# by default : row major " order = 'C"
