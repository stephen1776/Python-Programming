'''
5.15 (Find the largest n such that n^3 < 12,000) Use a while loop to find the largest
integer n such that n^3 is less than 12,000.
'''

i = 1

while i**3 < 12000:
    i += 1

print("This number is", i-1)
