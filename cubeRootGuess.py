cube = 270000
epsilon = 0.1
guess = 0
increment = 0.00001
numGuesses = 0
cutoff = 50000000

while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    guess += increment
    numGuesses += 1

    if numGuesses == cutoff:
        print(f'Did not find in {cutoff} tries, abandoning loop')
        break



if abs(guess**3 - cube) >= epsilon:
    print(f'Took {numGuesses} tries')
    print(f'failed on cube root of {cube}')
    print(f'guess was: {guess}')

else:
    guess = round(guess, 5)
    print(f'Took {numGuesses} tries to find approximate cube root')
    print(f'{guess} is close to the cube root of {cube}')
