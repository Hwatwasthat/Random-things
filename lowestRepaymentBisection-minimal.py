import math

def remainingBalance(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    originalBalance = balance
    lowestBound = balance / 12
    highestBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
    while True:
        i = 0
        balance = originalBalance
        testValue = (lowestBound + highestBound) / 2
        while i != 12:
            monthlyUnpaidBalance = balance - testValue
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            i += 1
        if balance < -0.01:
            highestBound = testValue
        elif balance > 0.01:
            lowestBound = testValue
        elif (balance < 0.01) and (balance > -0.01):
            break
    print(f'Lowest Payment: {round(testValue, 2)}')


remainingBalance(2500, 0.219)
