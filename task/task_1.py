char = input("Enter a character: ").lower()

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print(f"{char} is not a valid alphabet character.")


