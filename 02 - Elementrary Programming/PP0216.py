'''
2.16 (Physics: acceleration) Average acceleration is defined as the change of velocity
divided by the time taken to make the change, as shown in the following formula:
a = (v1 - v0) / t
Write a program that prompts the user to enter the starting velocity v0 in
meters/second, the ending velocity v1 in meters/second, and the time span t in
seconds, and displays the average acceleration.
'''
v0, v1, t = eval(input("Enter v0, v1, and t: "))
a = (v1 - v0) / t
print("The average acceleration is " + str(a) + " m/s^2")