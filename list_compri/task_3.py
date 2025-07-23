# 11. Reverse all strings in a list
string = ["hello", "world"]
reversed_str = [s[::-1] for s in string]
print("Reversed strings:", reversed_str)

# 12. Get the length of each word in a list
words = ["apple", "banana", "mango"]
length = [len(w) for w in words]
print("Lengths:", length)

# 13. Filter out all odd numbers from 0 to 19
even = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", even)

# 14. Remove empty strings from a list
string = ["apple", "", "banana", "", "mango"]
noempty = [s for s in string if len(s) != 0]
print("Non-empty strings:", noempty)

# 15. Convert a list of temperatures from Celsius to Fahrenheit
cel = [0, 20, 37, 100]
fah = [(c * 9/5) + 32 for c in cel]
print("Fahrenheit:", fah)

# 16. Count vowels in a word
word = "Hello"
vowels = "aeiouAEIOU"
count = sum(1 for ch in word if ch in vowels)
print("Vowel count in '{}': {}".format(word, count))

# 17. Convert a list of numbers to strings
numbers = [1, 2, 3, 4, 5]
int_str = [str(n) for n in numbers]
print("String numbers:", int_str)

# 18. Extract all capital letters from a sentence
string = "Hello World"
cap = [ch for ch in string if ch.isupper()]
print("Capital letters:", cap)

# 19. Double each number in a list
nums = [1, 2, 3, 4, 5]
dbl = [n * 2 for n in nums]
print("Doubled numbers:", dbl)

# 20. Filter names that are longer than 4 characters
names = ["xyz", "John Cena", "mark", "heh", "Bob the builder"]
long = [n for n in names if len(n) > 4]
print("Names longer than 4 characters:", long)
