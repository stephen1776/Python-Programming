'''
6.3 (Palindrome integer) Write the functions with the following headers:
def reverse(number):
# Return the reversal of an integer, e.g. reverse(456) returns 654

def isPalindrome(number):
# Return true if number is a palindrome

Use the reverse function to implement isPalindrome. A number is a palindrome
if its reversal is the same as itself. Write a test program that prompts the
user to enter an integer and reports whether the integer is a palindrome.
'''

def reverse(number):
    reverse_num = str(number)[::-1]
    number = str(number)
    return isPalindrome(number, reverse_num)

def isPalindrome(number, reverse_num):
    if number == reverse_num:
        print(number, "is a palindrome")
    else:
        print(number, "is not a palindrome")


def main():
    num = eval(input("Enter an integer: "))
    reverse(num)

if __name__ == '__main__':
    main()