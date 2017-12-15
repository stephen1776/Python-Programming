'''
6.14 (Estimate pi) can be computed using the following series:
 pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + (-1)^(i+1) / (2i - 1)
 Write a function that returns m(i) for a given i and write a test program that displays a table.
'''

def main():
    print(format("i", "<15s"), format("m(i)", "<20s"))
    print("----------------------")
    for i in range(1, 1000, 100):
        print(format(i, "<15d"), format(m(i), "<20.4f"))

def m(i):
    pi = 0
    sign = 1
    for i in range(1, i + 1, 1):
        pi += sign / (2 * i - 1)
        sign = -1 * sign

    return 4 * pi

if __name__ == '__main__':
    main()



