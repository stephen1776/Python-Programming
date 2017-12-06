'''
3.9 (Financial application: payroll) Write a program that reads the following information
and prints a payroll statement:
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%)
State tax withholding rate (e.g., 9%)

A sample run is shown below:
Enter employee's name:
Enter number of hours worked in a week:
Enter hourly pay rate:
Enter federal tax withholding rate:
Enter state tax withholding rate:

Output:
Employee Name: Smith
Hours Worked: 10.0
Pay Rate: $9.75
Gross Pay: $97.5
Deductions:
Federal Withholding (20.0%): $19.5
State Withholding (9.0%): $8.77
Total Deduction: $28.27
Net Pay: $69.22
'''

# Get data
employee_name = input("Enter employee’s name: ")
hours_worked = eval(input("Enter number of hours worked in a week: "))
hourly_rate = eval(input("Enter hourly pay rate: "))
fed_tax_rate = eval(input("Enter federal tax withholding rate: "))
state_tax_rate = eval(input("Enter state tax withholding rate: "))

# Calculate Deductions
gross_pay = hours_worked * hourly_rate
fed_withholding = round(gross_pay * fed_tax_rate * 0.01,2)
state_withholding = round(gross_pay * state_tax_rate * 0.01,2)
total_deductions = fed_withholding + state_withholding
net_pay = gross_pay - total_deductions

# Display results
print("\nEmployee Name: " + employee_name +
      "\nHours Worked: " + str(hours_worked) +
      "\nPay Rate: $" + str(hourly_rate) +
      "\nGross Pay: $" + str(gross_pay) +
      "\nDeductions:" +
      "\n\tFederal Withholding (" + str(fed_tax_rate) +"%): $" + str(fed_withholding) +
      "\n\tState Withholding (" + str(state_tax_rate) + "%): $" + str(state_withholding) +
      "\n\tTotal Deduction: $" + str(total_deductions) +
      "\nNet Pay: $" + str(net_pay)
)



