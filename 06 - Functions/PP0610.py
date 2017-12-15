'''
6.10 (Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides the
isPrime(number) function for testing whether a number is prime. Use this
function to find the number of prime numbers less than 10,000.
'''
#  Check if number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime


def main():
    count = 0
    N = 10000
    for number in range(2, N):
        if isPrime(number) == True:
            count += 1

    print("The number of prime numbers <", 10000, "is", count)

if __name__ == '__main__':
    main()