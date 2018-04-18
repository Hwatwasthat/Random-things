import random, sys, transpositionEncrypt, transpositionDecrypt


def main():
    # random.seed(34) # Set the random "seed" to a static value

    for i in range(20): # Set number of tests
        # Generate random numbers to test

        # The message will have a random length
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list and shuffle it
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # convert back to a string

        print(f'Test {i + 1}: "{message[:50]}..."')

        # Check all possible keys for the message
        for key in range(1, int(len(message) / 2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # If decrypted doesn't match message, display an error and quit
            if message != decrypted:
                print(f'Mismatch with key {key} and message {message}.')
                print(f'Decrypted as: {decrypted}')
                sys.exit()

    print('Transposition cipher test passed')

# If run as module
if __name__ == '__main__':
    main()
