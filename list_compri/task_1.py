# 1. Get squares of numbers from 1 to 10.
# 2. List all even numbers between 1 and 20.
# 3. Convert all strings in a list to uppercase.
# 4. Filter numbers divisible by 3 from a list.
# 5. Remove vowels from a given string.
# 6. Create a list of (number, square) tuples fro
# 7. Flatten a 2D list into a 1D list.
# 8. Replace negative numbers in a list with 0.
# 9. Find common elements between two lists.
# 10. Extract digits from a string.

squares = [x**2 for x in range(1, 11)]
print(squares)

even=[x for x in range(0, 20) if(x%2==0)]
print(even)

lst=["cjebebcb","kjsbac"]
print([i.upper() for i in lst])

lst=[3,5,6,78,52,12,356,45]
print([x for x in lst if(x%3 == 0)])

lst=['a','b','c','d','e']
[lst.remove(x) for x in lst if(x.lower()=='a' or x.lower()== 'e' or x.lower()=='i' or x.lower()=='o' or x.lower()=='u')]
print(lst)

tp=[(x,x**2) for x in range(0,6)]
print(tp)

lst1 = [[1,2],[3,4]]
lst2=[x for s in lst1 for x in s]
print(lst2)

lst = [1, -2, 3, -8, 5, -50, 10, 12]
result = [0 if x < 0 else x for x in lst]
print(result)

digits = [int(char) for char in 'a1b2c3d4' if char.isdigit()]
print(digits)

common = [x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]]
print(common)