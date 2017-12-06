'''
4.3 (Algebra: solve linear equations)
You can use Cramer’s rule to solve the
following system of linear equation:
Write a program that prompts the user to enter a, b, c, d, e, and f and display the
result. If ad – bc is 0, report that The equation has no solution.
'''
import math

a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
denominator = a*d - b*c

if denominator == 0:
    print("The equation has no solution.")
else:
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    print("x is " + str(x) + " and y is " + str(y))