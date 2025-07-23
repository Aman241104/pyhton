# # 1. ZeroDivisionError
# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError as z:
#     print(z)

# # 2.TypeError
# z=10
# x="royal"
# try:
#     e=z+x
#     print(e)
# except TypeError as t:
#     print(t)

# # 3.ValueError
# try:
#     z=int(10)
#     x=int("royal")
# except TypeError as t:
#     print(t)

# 4.file not found:
# try:
#     with open('x.json','r') as file:
#         pass
# except FileNotFoundError as f:
#     print(f)

# 5.NameError
try:
    print(aa)
except NameError as n:
    print(n)

# 6.ImportError
try:
    import data;
except ImportError as i:
    print(i)

