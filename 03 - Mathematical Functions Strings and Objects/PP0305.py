'''
3.5 (Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in
which all sides are of the same length and all angles have the same degree (i.e., the
polygon is both equilateral and equiangular). The formula for computing the area
of a regular polygon is

Area = (n * s^2) / ( 4 * tan(pi/n) )

Here, s is the length of a side. Write a program that prompts the user to enter the
number of sides and their length of a regular polygon and displays its area. Here is
a sample run:
Enter the number of sides: 5
Enter the side: 6.5
The area of the polygon is 73.69017017488385
'''
import math

num_sides = eval(input("Enter the number of sides: "))
side_length = eval(input("Enter the side length: "))

area = (num_sides * side_length**2) / ( 4 * math.tan(math.pi/num_sides) )

print("The area of the polygon is " + str(area))