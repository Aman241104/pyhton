import numpy as np

m1 = np.arange(1, 11).reshape(5, 2)
m2 = np.arange(11, 21).reshape(5, 2)
m3 = np.arange(21, 31).reshape(5, 2)

# h = np.hstack((m1, m2, m3))
v = np.vstack((m1, m2, m3))
# print("Horizontal,\n", h)
print("\nVertical,\n", v)
