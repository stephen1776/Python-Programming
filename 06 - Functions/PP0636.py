'''
6.36 (Generate random characters) Use the functions in RandomCharacter in
Listing 6.11 to print 100 uppercase letters and then 100 single digits, printing ten
per line.
'''
from random import randint # import randint

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

# Generate a random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')


N = 100

count = 1
for i in range(N):
    if count % 10 == 0:
        print(getRandomUpperCaseLetter())
    else:
        print(getRandomUpperCaseLetter(), end=" ")
    count += 1

for i in range(N):
    if count % 10 == 0:
        print(getRandomDigitCharacter())
    else:
        print(getRandomDigitCharacter(), end=" ")
    count += 1
