
month = int(input("Enter a month number (1-12): "))

match month:
    case 11|12|1|2:
        print("Winter")
    case 3|4|5|6:
        print("SUmmer")
    case 7|8|9|10:
        print("Monsoom")
    case _:
        print("Invalid month. Please enter a number from 1 to 12.")