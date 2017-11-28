'''
2.2 (Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * π
volume = area * length
'''

# Enter radius of the cylinder
radius, length  = eval(input("Enter the radius and length of a cylinder: "))

area = radius * radius * 3.14159
volume = area * length

print("The area is " + str(area))
print("The volume of the cylinder is " + str(volume))