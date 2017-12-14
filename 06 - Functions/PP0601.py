'''
6.1 (Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for
n = 1, 2, .... The first few numbers are 1, 5, 12, 22, ....
Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
'''

def getPentagonalNumber(n):
    y = []
    count = 0
    num_per_line = 10
    for i in range(1,n+1):
        x = int(i * (3*i - 1) / 2)
        y.append(x) # store 10 nums in an array
        # Display the 10 numbers and advance to a new line
        count += 1
        if count % num_per_line == 0:
            print(*y)
            y = []# Restart with new 10 to save


def main():
    n = 100
    getPentagonalNumber(n)


if __name__ == '__main__':
    main()

