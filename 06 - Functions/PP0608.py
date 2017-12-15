'''
6.8 (Conversions between Celsius and Fahrenheit) Write a module that contains the
following two functions:

def celsiusToFahrenheit(celsius):
# Converts from Celsius to Fahrenheit

def fahrenheitToCelsius(fahrenheit):
# Converts from Fahrenheit to Celsius
The formulas for the conversion are:
celsius = (5 / 9) * (fahrenheit – 32)
fahrenheit = (9 / 5) * celsius + 32
'''

# Convert from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    fahrenheit = (9.0 / 5.0) * celsius + 32
    return fahrenheit

# Convert from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius


def main():
    print(format("Celsius", "<15s"), format("Fahrenheit", "<15s"), "  |    ", format("Fahrenheit", "<15s"),
          format("Celsius", "<15s"))
    print("---------------------------------------------------------------")

    celsius = 40
    fahrenheit = 120
    i = 1

    while i <= 10:
        print(format(celsius, "<15d"), format(celsiusToFahrenheit(celsius), "<15.2f"), "  |    ",
              format(fahrenheit, "<15d"), format(fahrenheitToCelsius(fahrenheit), "<15.2f"))
        celsius -= 1
        fahrenheit -= 10
        i += 1

if __name__ == '__main__':
    main()
