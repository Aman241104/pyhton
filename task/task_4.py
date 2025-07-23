terms = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(f"Fibonacci sequence: {a}")
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1
