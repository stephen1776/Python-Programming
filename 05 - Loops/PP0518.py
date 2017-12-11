'''
5.18 (Find the factors of an integer) Write a program that reads an integer and displays
all its smallest factors, also known as prime factors. For example, if the input integer
is 120, the output should be as follows:
2, 2, 2, 3, 5
'''
# Enter a positive integer
number = eval(input("Enter a positive integer: "))

# Find the smallest factors of that integer
print("The factors for", number, "is", end=" ")
factor = 2
while factor <= number:
    if number % factor == 0:
        number = number / factor
        print(factor, end=" ")
    else:
        factor += 1
