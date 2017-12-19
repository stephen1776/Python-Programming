'''
6.26 (Mersenne prime) A prime number is called a Mersenne prime if it can be written
in the form for some positive integer p. Write a program that finds all
Mersenne primes with p <= 19 and displays the output as follows:
p 2^p - 1
2 3
3 7
5 31
...
'''
import time

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1

    return True  # number is prime


def main():
    beginTime = time.time()
    print("P " + "  2^P - 1")
    for p in range(2, 19 + 1):
        i = 2 ** p - 1
        if isPrime(i):
            print(str(p) + "\t" + str(i))

    endTime = time.time()
    print("Time spent is " + str(endTime - beginTime) + " milliseconds")

if __name__ == '__main__':
    main()
