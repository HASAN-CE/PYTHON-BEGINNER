# F = (C × 9/5) + 32


Celsius = int(input('Enter the Celsius temperature: '))

def f_to_c(Celsius):
    Fahrenheit = (Celsius * 9/5)+32
    return Fahrenheit

print("Temperature in Fahrenheit is: ",round(f_to_c(Celsius)))