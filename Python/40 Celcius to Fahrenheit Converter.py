"""Celcius to Fahrenheit Converter.py
You are making a Celcius to Fahrenheit converter.
Write a function to take Celsius value as an argument
and return the corresponding Fahrenheit value.

F = 9/5 * C + 32

For my purposes I will be doing the inverse as well.
"""

def celsius_to_fahrenheit(celsius:float) -> float:
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit

# F = 9/5C + 32
# F - 32 = 9/5C
# (F - 32)*5/9 = C
# 5/9F - 160/9 = C
def fahrenheit_to_celsius(fahrenheit:float) -> float:
    celsius = (5/9 * fahrenheit) - 160/9
    return celsius

print(celsius_to_fahrenheit(-40))
print(fahrenheit_to_celsius(-40))

print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celsius(0))

print(celsius_to_fahrenheit(38))
print(fahrenheit_to_celsius(38))

print(celsius_to_fahrenheit(46))