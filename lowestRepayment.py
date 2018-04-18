import math

def remainingBalance(balance, annualInterestRate):
    """
    This calculates the minimum payment for repaying a credit card/ loan
    """

    # Establish values to be used
    monthlyInterestRate = annualInterestRate / 12
    originalBalance = balance

    # They want it worked out in steps of 10, so its more complicated than necessary
    guess = math.ceil((balance / 12) /10) * 10
    
    

    while True:
        # Set initial values, reset after 1st run
        i = 0
        balance = originalBalance

        # Loop to see if current amount is adequate
        while i != 12:
            monthlyUnpaidBalance = balance - guess
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            i += 1

        # Check result. Always starts low so no need for a lower bounds case, if not
        # sufficient, reset. If sufficient, break out of loop.
        if balance < 0:
            break
        else:
            guess += 10

    # Print the result
    print('Lowest Payment: {}'.format(guess))


remainingBalance(50000000000, 0.2)
