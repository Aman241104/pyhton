# pip install pandas

# from operator import index
import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
# print(a)

# print(a[0])

# indexing
# b = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(b)

# Pandas provides two primary data structures:

# Series : 1-dimensional labeled array (like a column)

# DataFrame : 2-dimensional labeled data table (like an Excel sheet)

# It is built on top of NumPy and makes working with structured data fast, flexible, and expressive.


# A Series is a one-dimensional labeled array capable of holding:

# Integers

# Floats

# Strings

# Any Python objects

# Series like a column in Excel or a single column in a DataFrame.

# a = (['a', 'b', 'c'])
# b = ([1, 2, 3])
# s = pd.Series(b, index=a, name='pandas', dtype=float)
# print(s)



a = pd.Series([1, 2, 3, 4, 5])
# print(a)
a = pd.Series([1, 2, 3, 4, 5], dtype='float')
# print(a)
a = pd.Series([1, 2, 3, 4, 5], dtype='str')
# print(a)
a = pd.Series([1, 2, 3, 4, 5], dtype='bool')
# print(a)


a = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(a[a > 3][a < 7])


# print(min(a))
# print(max(a))


a = []
for i in range(1, 30):
    a.append(i)
# print(a)

x = pd.Series(a)
# print(x)


a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([1, 2, 3, 4, 5])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a % b)



a = pd.Series({1: 'a', 2: 'b'})
print(a)