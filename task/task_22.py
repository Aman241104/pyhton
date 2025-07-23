# Perfect Number by using For_loop
for i in range(0,10000):
    Input_Number = i
    Sum = 0
    for i in range(1, Input_Number):
        if(Input_Number % i == 0):
            Sum = Sum + i
    if (Sum == Input_Number):
        print(f"{Input_Number} is a perfect number.")
