'''
6.13 (Sum series) Write a function to compute the following series:
m(i) = 1/2 + 2/3 + ... + i/(i + 1)
Write a test program that displays a table.
'''

def main():
    print(format("i", "<15s"), format("m(i)", "<20s"))
    print("------------------------")
    for i in range(1, 20+1, 1):
        print(format(i, "<15d"), format(m(i), "<20.4f"))


def m(i):
    sum = 0
    for i in range(1, i + 1):
        sum += i / (i + 1)

    return sum

if __name__ == '__main__':
    main()