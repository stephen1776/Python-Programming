'''
5.23 (Financial application: compare loans with various interest rates) Write a program
that lets the user enter the loan amount and loan period in number of years
and displays the monthly and total payments for each interest rate starting from
5% to 8%, with an increment of 1/8.
'''

# Enter loan amount
loanAmount = eval(input("Enter loan amount: "))

# Enter number of years
numOfYears = eval(input("Enter number of years as an integer: "))

# Display the header
print(format("Interest Rate", "<15s"), format("Monthly Payment", "<15s"), format("Total Payment", "<15s"))
annualInterestRate = 5.0
i = 0
while i <= 24:
    # Calculate payment
    monthlyInterestRate = annualInterestRate / 1200
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numOfYears * 12))
    totalPayment = monthlyPayment * numOfYears * 12

    # Print Results
    print(format(annualInterestRate, "<15.3f"), format(monthlyPayment, "<15.2f"), format(totalPayment, "<15.2f"))

    # Increment
    annualInterestRate += 1 / 8
    i += 1
