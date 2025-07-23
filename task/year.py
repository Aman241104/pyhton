
year = int(input("Enter The Year:"))

if (year % 400 == 0) or (year%100 != 0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")