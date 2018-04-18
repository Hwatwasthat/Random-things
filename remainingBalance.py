import math

def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    This calculates the remaining balance on a card if only the minimum
    payment is done. First steps is to get the monthly interest. Then
    enter a while loop that runs through for each month, figure out the
    changing values (min monthly payment, remaining balance) and then
    alters balance to reflect these. Once loop is left use round to make
    the output only 2 decimal points.
    """
    i = 0
    monthlyInterestRate = annualInterestRate / 12

    while i != 12:
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        i += 1

    # only round for printing, if rounded during maths calculations go wrong
    balancePrint = round(balance, 2)
    print(f'Remaining balance: {balancePrint}')


remainingBalance(484, 0.2, 0.04)
