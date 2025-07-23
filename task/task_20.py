#while numerator <= 97 and denominator <= 99:
numerator = 1
denominator = 3
total_sum = 0

while numerator <= 97 and denominator <= 99:
    total_sum += numerator / denominator
    numerator += 2
    denominator += 2
print(f"The sum of the series is: {total_sum:.6f}")