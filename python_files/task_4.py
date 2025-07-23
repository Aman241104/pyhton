import os

# with open('vowels.txt','w') as file:
#     file.write("asdfghjkl")
#     file.close()

vowels = "aeiouAEIOU"
count = 0

# filename = input("Enter file name to read: ")
if os.path.exists('reportcard.txt'):
    with open('reportcard.txt', 'r') as file: 
        for char in file.read():
            print(char)
            if char in vowels:
                count += 1
        file.close()
else:
    print("File does not exist.")

print("Total vowels:", count)