'''
6.5 (Sort three numbers) Write the following function to display three numbers in
increasing order:
def displaySortedNumbers(num1, num2, num3):
Write a test program that prompts the user to enter three numbers and invokes the
function to display them in increasing order
'''
def displaySortedNumbers(num1, num2, num3):
    if num1 <= num2 <= num3:
        print("The sorted numbers are", num1, num2, num3)

    elif num2 <= num1 <= num3:
        print("The sorted numbers are", num2, num1, num3)

    elif num1 <= num3 <= num2:
        print("The sorted numbers are", num1, num3, num2)

    elif num3 <= num1 <= num2:
        print("The sorted numbers are", num3, num1, num2)

    elif num2 <= num3 <= num1:
        print("The sorted numbers are", num2, num3, num1)

    else: # num3 <= num2 <= num1
        print("The sorted numbers are", num3, num2, num1)

def main():
    num1, num2, num3, = eval(input("Enter 3 numbers (seperated by commas): "))
    displaySortedNumbers(num1, num2, num3)

    # Easier way:
    # x = [num1,num2,num3]
    # x.sort(key=int)
    # print(*x)

if __name__ == '__main__':
    main()


