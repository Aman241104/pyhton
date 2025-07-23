# 11. Reverse all strings in a list.
# 12. Get the length of each word in a list.
# 13. Filter out all odd numbers from 0 to 19.
# 14. Remove empty strings from a list.
# 15. Convert a list of temperatures from Celsius to Fahrenheit.

str = ["hello", "world"]
rev = [s[::-1] for s in str]
print(rev)

words = ["hello", "world"]
lengths = [len(word) for word in words]
print(lengths)

even = [num for num in range(20) if num % 2 == 0]
print(even)

str = ["hello", "", "world"]
nonempty_str = [s for s in str if s]
print(nonempty_str)

cel = [0, 20, 30, 40]
fah = [(temp * 9/5) + 32 for temp in cel]
print(fah)

