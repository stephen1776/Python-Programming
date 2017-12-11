'''
5.16 (Compute the greatest common divisor) First find d to
be the minimum of n1 and n2, and then check whether d, d - 1, d - 2, ..., 2, or
1 is a divisor for both n1 and n2 in this order. The first such common divisor is the
greatest common divisor for n1 and n2.
'''
# Enter n1 and n2
n1 = eval(input("Enter the first number: "))
n2 = eval(input("Enter the second number: "))

# Find minimum of n1 and n2
if n1 < n2:
    d = n1
else:
    d = n2

# Check whether d, d - 1, d - 2, ..., 2, or 1 is a divisor for both n1 and n2 in this order
while d >= 1:
    if n1 % d == 0 and n2 % d == 0:
        break
    d -= 1

print("GCD of", n1, "and", n2, "is", d)