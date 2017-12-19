'''
6.25 (Emirp) An emirp ( prime spelled backward) is a nonpalindromic prime number
whose reversal is also a prime. For example, both 17 and 71 are prime numbers, so
17 and 71 are emirps. Write a program that displays the first 100 emirps. Display
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



def isEmirp(number):
    return number != reverse(number) and isPrime(reverse(number))


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

        if isPrime(i) and isEmirp(i):
            print(i, end=" ")

            if count % 10 == 0: # 10 primes per line
                print()

            count += 1  # Increase count

        i += 1


if __name__ == '__main__':
    main()

