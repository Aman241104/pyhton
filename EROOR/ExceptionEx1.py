# exception :
# runtime error 

# TypeError
# valueError

# 1. deiveide by Zero/ ZeroDivisionError

a = 40
b = 0
# try:
#     c= a/b
#     print(c)
# except:
#     print("ZeroDivisionError")

# try:
#     c= a/b
#     print(c)
# except ZeroDivisionError as e: 
#     print(e)
    
# 2. TypeError
# a = 20
# b = "royal"
# try:
#     c = a+b
#     print(c)
# except TypeError as e :
#     print(e)
#     print("int only pls")
    
# 3. ValueError:
# a = int(23.90)
# b = int('royal')
# try:
#     c = a+b
#     print(c)
# except ValueError as v:
#     print(v)
#     print("int nakho khali")

# 4. IndexError
lst = [1,2,3,4]
try:
    print(lst[9])
except IndexError as i:
    print(i)

print("After exception")