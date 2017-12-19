'''
6.35 (Compute the probability) Use the functions in RandomCharacter in Listing
6.11 to generate 10,000 uppercase letters and count the occurrence of A.
'''
from random import randint # import randint

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# Generate a random uppercase letters
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

def calcAContent():
    u_letters = ""
    for i in range(1,10000+1):
        u_letters += getRandomUpperCaseLetter()
        a_count = u_letters.count('A')
        a_prob = a_count / len(u_letters)
        results = [a_count, a_prob, len(u_letters)]
    return results


def main():
    x = calcAContent()
    print("The probability of A is",x[1],)
    print("The A count is", x[0], "out of", x[2])

if __name__ == '__main__':
    main()


