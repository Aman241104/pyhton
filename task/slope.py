# Write a program to compute the slope of a line between two points (x1, y1) and (x2, y2).
print("Enter coordinates of the first point (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Enter coordinates of the second point (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

slope = (y2 - y1) / (x2 - x1)

print(f"The slope of the line between the points ({x1}, {y1}) and ({x2}, {y2}) is: {slope}")
