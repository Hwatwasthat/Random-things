import transpositionEncrypt, transpositionDecrypt, sys, pyperclip

def main():
    # Dictionary storing references for the menu. Easierr than an if, else sorter.
    # They have no brackets as they will run instantly if they do! that is why
    # myDict[choice] below ends with brackets. Still not sure how to simplify menu
    # so I can only need to update the dictionary.
    myDict = {1: encryptTextInterface, 2: decryptTextInterface, 3:sys.exit}
    while True:
        print('Menu:\
             \n1. Encrypt\
             \n2. Decrypt\
             \n3. Exit\n')
        choice = int(input('Please select which function you would like to use:'))
        myDict[choice]()
        

def encryptTextInterface():
    message = input('Please enter text to be encrypted:')
    key = int(input('Please enter length of key to use:'))
    ciphertext = transpositionEncrypt.encryptMessage(key, message)
    print(ciphertext + '\n')
    pyperclip.copy(ciphertext)

def decryptTextInterface():
    message = input('Please enter text to be decrypted:')
    key = int(input('Please enter length of key to use:'))
    plaintext = transpositionDecrypt.decryptMessage(key, message)
    print(plaintext)
    pyperclip.copy(plaintext + '\n')

main()
