quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01

quarters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickels = int(input("Enter the number of nickels: "))
pennies = int(input("Enter the number of pennies: "))

total_dollars = (quarters * quarter_value) + (dimes * dime_value) + (nickels * nickel_value) + (pennies * penny_value)
print(f"The total value of change is: ${total_dollars:.2f}")
