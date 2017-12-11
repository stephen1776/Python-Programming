'''
5.42 (Monte Carlo simulation) A square is divided into four smaller regions.
If you throw a dart into the square one million times, what is the probability for
the dart to fall into an odd-numbered region? Write a program to simulate the
process and display the result.
'''
import random

NUMBER_OF_TRIALS = 1000000 # If throw a dart into the square one million times
numberOfHits = 0

for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2.0 - 1;
    y = random.random() * 2.0 - 1;
    if x < 0:
        numberOfHits += 1
    elif not (x > 1 or x < 0 or y > 1 or y < 0):
        slope = (1.0 - 0) / (0 - 1.0)
        x1 = x + -y * slope
        if x1 <= 1:
          numberOfHits += 1

print("The probability for the dart to fall into Regions 1 and 3 is",
    1.0 * numberOfHits / NUMBER_OF_TRIALS)
