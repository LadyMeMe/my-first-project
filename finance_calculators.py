# Finance Calculator Capstone Project
# This program calculates investment returns and bond repayments.

import math
# This is the menu options for the user
print("Investment-to calculate the amount of investment you'll earn on your investment.")
print("Bond- to calculate the amount you'll have to pay on a home loan.")

# Ask the user what calculator they want to use
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:") .lower()

if choice == "investment":
    # Ask the user for the investment information
    deposit = float(input(" Enter the deposit amount:"))
    interest_rate = float(input(" Enter the interest rate:"))
    years = int(input("Enter the number of years:"))

    interest = input("Do you want simple or compound interest ").lower()

    # Convert percentage to decimal
    r = interest_rate/100

    if interest == "simple":
        total_amount = deposit * (1 + r * years)
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + r), years)
    else:
        print("Invalid interest type.")
        exit()
        print(f"The total amount after interest rate is {total_amount:.2f}")

elif choice == "bond":
    # Ask the user for the bond information
    house_value= float(input("Enter the house value: "))
    interest_rate = float(input("Enter the interest rate:"))
    months = int(input("Enter the number of months to repay the bond: "))

    # Calculate monthly interest rate
    i = (interest_rate/100) / 12

    # Calculate monthly repayment plan
    repayment = ( i * house_value) / (1 - ( 1 + i) ** (-months))
    print(f"The repayment amount is {repayment:.2f}")
# Completed the Finance Calculator Capstone project
