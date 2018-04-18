# Transposition cipher decrpytion

import math, pyperclip

def main():
    myMessage = input('What would you like deciphered?:\n')
    myKey = int(input('What size key is used?:\n'))

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | (called a pipe) after in case there are
    # spaces at the end of the decrypted message
    print('\n' + plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function simulates the "columns"
    # and "rows" of the grid that the plaintext is written on by
    # using a list of strings. First, we need to calculate a few values.

    # The number of "Columns" in the transposition grid
    numOfColumns = int(math.ceil(len(message) / float(key)))

    # Number of "rows" in our grid
    numOfRows = key

    # number of "shaded boxes" in last "column" of the grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid
    plaintext = [''] * numOfColumns

    # The character and row variables point to where in the grid the next
    # character in the encrypted message will go
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # point to next column

        # If there are no more columns OR we're at a shaded box, go back
        # to the first column and next row
        if (column == numOfColumns) or (column == numOfColumns - 1 and row
                                        >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

# If transpositionDecrypt.py is run (instead of imported) call main()
if __name__ == '__main__':
    main()
