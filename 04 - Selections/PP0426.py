'''
4.26 (Palindrome number) Write a program that prompts the user to enter a three-digit
integer and determines whether it is a palindrome number. A number is a palindrome
'''
number = eval(input("Enter a three-digit integer: "))

if str(number) == str(number)[::-1]:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")
