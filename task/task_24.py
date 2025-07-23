# Write a program to calculate simple and compound interest.

print("Enter the details for interest calculation:")
principal = float(input("Principal amount: "))
rate = float(input("Rate of interest (in %): "))
time = float(input("Time (in years): "))


simple_interest = (principal * rate * time) / 100
compound_am = (principal * (1 + rate / 100) ** time)
c_i= compound_am - principal

print(f"\nSimple Interest: {simple_interest:.2f}")
print(f"Compound Interest: {c_i:.2f}")


