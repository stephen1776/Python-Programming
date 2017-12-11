'''
(Compute e) You can approximate e by using the following series:
e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000, ..., and 100000.
'''
e = 1
prev_e = 1

for i in range(1, 100000 + 1):
    prev_e = prev_e / i
    e += prev_e

    if i == 10000 or i == 20000 or i == 30000 or i == 40000 or i == 50000 or i == 60000 or i == 70000 or i == 80000 \
        or i == 90000 or i == 100000:
        print("The value of e is ", e, " for i = ", i)
