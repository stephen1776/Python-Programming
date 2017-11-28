'''
2.8 (Science: calculate energy) Write a program that calculates the energy needed to
heat water from an initial temperature to a final temperature. Your program should
prompt the user to enter the amount of water in kilograms and the initial and final
temperatures of the water. The formula to compute the energy is
Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius,
and energy Q is measured in joules
'''
# Prompt the user to enter a degree in Celsius
mass = eval(input("Enter the amount of water in kilograms: "))

initialTemperature = eval(input("Enter the initial temperature: "))
    
finalTemperature = eval(input("Enter the final temperature: "))

energy =  mass * (finalTemperature - initialTemperature) * 4184

print("The energy needed is " + str(energy) + " Joules")