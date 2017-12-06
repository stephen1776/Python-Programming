'''
4.1 (Algebra: solve quadratic equations)
Write a program that prompts the user to enter values for a, b, and c and displays
the result based on the discriminant. If the discriminant is positive, display two
roots. If the discriminant is 0, display one root. Otherwise, display 'The equation
has no real roots.'
'''

import math

a, b, c = eval(input("Enter a, b, c: "))
discriminant = b**2 - 4*a*c

if discriminant > 0:
    root_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    root_2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The roots are " + str(root_1) + " and " + str(root_2))
elif discriminant == 0:
    root_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The root is " + str(root_1))
else:
    print("The equation has no real roots.")