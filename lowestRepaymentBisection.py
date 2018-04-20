<<<<<<< HEAD
import math

def remainingBalance(balance, annualInterestRate):
    """
    This calculates the minimum payment for repaying a credit card/ loan
    """

    # Establish values to be used
    monthlyInterestRate = annualInterestRate / 12
    originalBalance = balance

    # Create highest and lowest values to be tested from
    lowestBound = balance / 12
    highestBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
    

    while True:
        # Set initial values, reset after 1st run
        i = 0
        balance = originalBalance
        # Test value is a point halfway between monthly value of total cost with all interest
        # and monthly value without. After reset it changeds depending on variance from target
        testValue = (lowestBound + highestBound) / 2

        # Loop to see if current amount is adequate
        while i != 12:
            monthlyUnpaidBalance = balance - testValue
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            i += 1

        # Check result. First check if too high or too low, if sufficient, break out of loop.
        # If too low, reduce higher bound to tested value
        if balance < -0.01:
            highestBound = testValue

        # If too high, increase lower bound to tested value
        elif balance > 0.01:
            lowestBound = testValue

        # If within a cent of correct, leave loop
        elif (balance < 0.01) and (balance > -0.01):
            break

    # Print the result
    print('Lowest Payment: {}'.format(round(testValue, 2)))


remainingBalance(2500, 0.219)
=======
import math

def remainingBalance(balance, annualInterestRate):
    """
    This calculates the minimum payment for repaying a credit card/ loan
    """

    # Establish values to be used
    monthlyInterestRate = annualInterestRate / 12
    originalBalance = balance

    # Create highest and lowest values to be tested from
    lowestBound = balance / 12
    highestBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
    

    while True:
        # Set initial values, reset after 1st run
        i = 0
        balance = originalBalance
        # Test value is a point halfway between monthly value of total cost with all interest
        # and monthly value without. After reset it changeds depending on variance from target
        testValue = (lowestBound + highestBound) / 2

        # Loop to see if current amount is adequate
        while i != 12:
            monthlyUnpaidBalance = balance - testValue
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            i += 1

        # Check result. First check if too high or too low, if sufficient, break out of loop.
        # If too low, reduce higher bound to tested value
        if balance < -0.01:
            highestBound = testValue

        # If too high, increase lower bound to tested value
        elif balance > 0.01:
            lowestBound = testValue

        # If within a cent of correct, leave loop
        elif (balance < 0.01) and (balance > -0.01):
            break

    # Print the result
    print('Lowest Payment: {}'.format(round(testValue, 2)))


remainingBalance(2500, 0.219)
>>>>>>> 7e1264f782abda423dc21c11e901e4507678a674
