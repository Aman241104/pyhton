# A lambda function that takes three parameters and returns the product of all three.
# x= lambda a,b,c:a*b*c
# print(x(10,20,30))

# Use `filter()` to filter out even numbers from a list.
# lst=[0,1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda lst:lst%2 == 0,lst))
# print(x)

# Applying a lambda function to add 5 to every element in a list.
# lst=[1,2,3,4]
# x=list(map(lambda lst:(lst+5),lst))
# print(x)

# Sorting a List of Tuples
# data = [(1, 'b'), (3, 'a'), (2, 'b')]
# sorted_data = sorted(data,key=lambda x: x[1])
# print(sorted_data)

#string reverse
# str1= "ABCDEF"
# str2= (lambda str1:(str1[::-1])) 
# print(str2(str1)) 