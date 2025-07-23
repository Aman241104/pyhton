sum_of_evens = 0


for number in range(1, 51):
    if number % 2 == 0:
        sum_of_evens += number

print("The sum of all even numbers between 1 and 50 is:", sum_of_evens)
