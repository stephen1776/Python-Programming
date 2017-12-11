'''
5.25 (Demonstrate cancellation errors) A cancellation error occurs when you are
manipulating a very large number with a very small number. The large number
may cancel out the smaller number. For example, the result of 100000000.0 +
0.000000001 is equal to 100000000.0. To avoid cancellation errors and obtain
more accurate results, carefully select the order of computation. For example, in
computing the following series, you will obtain more accurate results by computing
from right to left rather than from left to right:
1 + 1/2 + 1/3 + ... + 1/n
Write a program that compares the results of the summation of the preceding
series, computing both from left to right and from right to left with n = 50000.
'''

n = 50000
sumLR = 0
for i in range(1, n + 1):
    sumLR += 1.0 / i

print("The sum from left to right is:", sumLR)

sumRL = 0
for i in range(0, n):
    sumRL += 1.0 / (n - i)

print("The sum from right to left is:", sumRL)