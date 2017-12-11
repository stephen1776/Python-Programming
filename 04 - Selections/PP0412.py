'''
4.12 (Check a number) Write a program that prompts the user to enter an integer and
checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just
one of them (but not both).
'''
number = eval(input("Enter an integer: "))

if number % 5 == 0 and number % 6 == 0:
    print(number, "is divisible by both 5 and 6")
elif number % 5 == 0 or number % 6 == 0:
    print(number, "is divisible by 5 or 6, but not both")
else:
    print(number, "is not divisible by either 5 or 6")
