def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    A perfect number equals the sum of its proper divisors (excluding itself).
    """
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def find_perfect_numbers(limit):
    """
    Find all perfect numbers less than the given limit.
    """
    perfect_numbers = []
    for num in range(2, limit):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

# Define the limit
limit = 10000

# Find perfect numbers less than the limit
perfect_numbers = find_perfect_numbers(limit)

# Display the result
print(f"Perfect numbers less than {limit}: {perfect_numbers}")
