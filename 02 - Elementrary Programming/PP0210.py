'''
2.10 (Physics: find runway length) Given an airplane’s acceleration a and take-off
speed v, you can compute the minimum runway length needed for an airplane to
take off using the following formula:
length = v^2/(2a)
Write a program that prompts the user to enter v in meters/second (m/s) and the
acceleration a in meters/second squared and displays the minimum runway
length.
'''
v, a = eval(input("Enter speed and acceleration: "))

length = v * v / (2 * a)
    
print("The minimum runway length for this airplane is " + str(length) + " meters")