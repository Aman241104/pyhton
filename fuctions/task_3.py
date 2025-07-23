def feettocm(x):
    feet_to_centimeters = 30.48
    centimeters = x * feet_to_centimeters
    print(f"{x} feet ={centimeters} cm")

def feettom(x):
    feet_to_meters = 0.3048
    meters = x * feet_to_meters
    print(f"{x} feet ={meters} m")

def feettoinch(x):
    feet_to_inches = 12
    inches = x * feet_to_inches
    print(f"{x} feet ={inches} m")

def feettoyards(x):
    feet_to_yards = 1 / 3
    yards = x * feet_to_yards
    print(f"{x} feet ={yards} m")

def feettokm(x):
    feet_to_kilometers = 0.0003048
    kilometers = x * feet_to_kilometers
    print(f"{x} feet ={kilometers} m")


x=int(input("Enter feet:"))
print("Enter 1 to convert in centimeters.")
print("Enter 2 to convert in meters.")
print("Enter 3 to convert in inchs.")
print("Enter 4 to convert in yards.")
print("Enter 5 to convert in kilometers.")
print("Enter 6 to exit.")
ch=int(input("Enter Your choice:"))

match ch:
    case 1:
        feettocm(x)
        break
    case 2:
        feettom(x)
        break
    case 3:
        feettoinch(x)
        break
    case 4:
        feettoyards(x)
        break
    case 5:
        feettokm(x)
        break