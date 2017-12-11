'''
5.22 (Display prime numbers between 2 and 1,000) Modify Listing 5.13 to display all
the prime numbers between 2 and 1,000, inclusive. Display ten prime numbers
per line.

'''

NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
count = 0 # Count the number of prime numbers
number = 2 # A number to be tested for primeness

print("The prime numbers between 2 and 1,000 are:")

# Repeatedly find prime numbers
while number <= 1000:
    # Assume the number is prime
    isPrime = True

    # Test if number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, the number is not prime
            isPrime = False  # Set isPrime to false
            break  # Exit the for loop
        divisor += 1

    # Display the prime number and increase the count
    if isPrime:
        count += 1 # Increase the count

        print(format(number, "4d"), end = "")
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to the new line
            print() # Jump to the new line

    # Increment then check if the next number is prime
    number += 1
