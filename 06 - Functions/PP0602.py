'''
6.2 (Sum the digits in an integer)
Write a function that computes the sum of the digits in an integer.
For example, sumDigits(234) returns 9 (2 + 3 + 4)
Write a test program that prompts the user to enter an integer and displays the sum of all its digits.
'''

def sumDigits(n):
    temp = abs(n)
    sum = 0

    while temp != 0:
        remainder = temp % 10
        sum += remainder
        temp = temp // 10 # remove the extracted digit

    return sum



def main():
    number = eval(input("Enter a number: "))

    print("The sum of digits for", number, "is:", sumDigits(number))



if __name__ == '__main__':
    main()
