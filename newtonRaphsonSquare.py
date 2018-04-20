def newtonRaphsonSquare(squareRootTarget = 1):
    """
    Takes a positive integer as in input, returns a float
    round to the 4th decimal placethat is the closest to
    the square root of the number using Newton-Raphson
    methodology. Returns error if not an integer.
    Defaults to 1 as input.
    """

    # Establishing constants
    epsilon = 0.01
    guess = squareRootTarget / 2.0
    numGuesses = 0

    # While loop that works through methodology
    while abs(guess * guess - squareRootTarget) >= epsilon:
        numGuesses += 1
        guess = guess -(((guess ** 2) - squareRootTarget) / (2 *guess))
        
    return round(guess, 4)


if __name__ == '__main__':
    newtonRaphsonSquare()
