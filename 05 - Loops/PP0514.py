'''
5.14 (Find the smallest n such that n^2 > 12,000) Use a while loop to find the smallest
integer n such that n^2 is greater than 12,000.
'''
i = 1

while i**2 <= 12000:
    i += 1

print("This number is", i)
