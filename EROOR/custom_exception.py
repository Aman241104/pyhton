class RainException(Exception):
    pass

try:
    raining = False
    print("Enter 1 if raining or 2 if not")
    a=int(input("Enter:"))
    if(a == 1):
        raining = True
    elif(a == 2):
        raining = False
    else:
        print("Enter valid input.")
    
    if raining:
        raise RainException("Cannot attend offline lecture because of rain *very sadd*")
    
    print("Attending lecture offline *yippee*")
    
except RainException as e:
    print(f"Error: {e}")