'''
2.6 (Sum the digits in an integer) Write a program that reads an integer between 0 and
1000 and adds all the digits in the integer. For example, if an integer is 932, the
sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the //
operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
10 = 93.)
'''
#  Read a number
number = eval(input("Enter an integer between 0 and 1000: "))

lastDigit = number % 10
remainingNumber = number // 10
secondLastDigit = remainingNumber % 10

remainingNumber = remainingNumber // 10
thirdLastDigit = remainingNumber % 10

# Obtain the sum of all digits
sum = lastDigit + secondLastDigit + thirdLastDigit

# Display results
print("The sum of all digits in " + str(number) + " is " + str(sum))