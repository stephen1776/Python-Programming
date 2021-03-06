'''
6.24 (Palindromic prime) A palindromic prime is a prime number that is also palindromic.
For example, 131 is a prime and also a palindromic prime, as are 313 and
757. Write a program that displays the first 100 palindromic prime numbers. Display
10 numbers per line.
'''


def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1

    return True  # number is prime


# Return the reversal of an integer, i.e. reverse(456) returns 654
def isPalindrome(number):
    return number == reverse(number)


# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result


def main():
    count = 1

    i = 2
    while count <= 100:
        # Display each number in five positions
        if isPrime(i) and isPalindrome(i):
            print(i, end=" ")

            if count % 10 == 0: # 10 primes per line
                print()

            count += 1  # Increase count

        i += 1


if __name__ == '__main__':
    main()

