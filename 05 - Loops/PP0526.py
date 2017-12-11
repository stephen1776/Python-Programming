'''
5.26 (Sum a series) Write a program to sum the following series:
1/3 + 3/5 + 5/7 + 7/9 + 9/11 + 11/13 + ... + 95/97 + 97/99
'''

sum = 0
for i in range(1, 97 + 1, 2):
    sum += 1.0 * i / (i + 2)

print("The sum is", sum)
