'''
6.4 (Display an integer reversed) Write the following function to display an integer in
reverse order:
def reverse(number):
For example, reverse(3456) displays 6543. Write a test program that prompts
the user to enter an integer and displays its reversal.
'''


def reverse(number):
    while number != 0:
        remainder = number % 10
        print(remainder, end = "") # Print the number at once on one line
        number = number // 10


def main():
    num = eval(input("Enter an integer: "))
    reverse(num)

if __name__ == '__main__':
    main()

