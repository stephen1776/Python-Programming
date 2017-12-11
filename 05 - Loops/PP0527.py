'''
5.27 (Compute pi) You can approximate by using the following series:
pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + (-1)^(i+1) / (2i - 1)
Write a program that displays the pi value for i = 10000, 20000, ..., and 100000.
'''
import math
pi = 0
for i in range(1, 100000 + 1):
    pi += 4.0 * (math.pow((-1), i + 1) / (2*i - 1))
    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 10 \
        or i == 10000 or i == 20000 or i == 30000 or i == 40000 or i == 50000 or i == 60000 or i == 70000 or i == 80000 \
        or i == 90000 or i == 100000:
        print("The value of pi is ", pi, " for i = ", i)



