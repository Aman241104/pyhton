#Write a program to convert temperature fromCelsius to Fahrenheit. Equation to convert Celsius To Fahrenheit:𝐹 = (9/5) * 𝐶 + 32
celsius = float(input("Enter temperature in Celsius: "))


fahrenheit = (9 / 5) * celsius + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")