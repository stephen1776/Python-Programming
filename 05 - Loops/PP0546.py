'''
5.46 (Statistics: compute mean and standard deviation) In business applications, you
are often asked to compute the mean and standard deviation of data. The mean is
simply the average of the numbers. The standard deviation is a statistic that tells
you how tightly all the various data are clustered around the mean in a set of data.
Write a program that prompts the user to enter ten numbers, and displays the mean and standard deviations
of these numbers.
'''
import math

COUNT = 10 # Total numbers
sum = 0 # Store the sum of the numbers
squareSum = 0 # Store the sum of the squares

# Create numbers, find its sum, and its square sum
for i in range(COUNT):
     # Get a new number
     number = eval(input("Enter a number: "))

     # Add the number to sum
     sum += number

     # Add the square of the number to squareSum
     squareSum += number ** 2 # Same as number*number

# Find mean
mean = sum / COUNT

# Find standard deviation
sd = math.sqrt((squareSum - sum * sum / COUNT) / (COUNT - 1))

# Display result
print("The mean is", mean)
print("The standard deviation is", sd)
