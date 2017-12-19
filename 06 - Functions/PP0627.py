'''
6.27 (Twin primes) Twin primes are a pair of prime numbers that differ by 2. For example,
3 and 5, 5 and 7, and 11 and 13 are twin primes. Write a program to find all
twin primes less than 1,000. Display the output as follows:
(3, 5)
(5, 7)
...
'''
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

def isTwinPrime(number):
    if isPrime(number) and isPrime(number + 2) == True:
        return number

def main():
    print("The twin primes less than 1000 are")
    for p in range(3,1000):
        if isTwinPrime(p):
            print("("+ str(isTwinPrime(p))+",", str(p+2)+")")


if __name__ == '__main__':
    main()
