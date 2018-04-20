# Transposition Ciper Encryption

import pyperclip as clip

def main():
    myKey = 0
    
    myMessage = input('What would you like enciphered?:\n')
    
    myKey = int(input('How long a key would you like to use?:\n'))
        
    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in Ciphertext to the screen
    # with a | ("pipe" character) after it in case there are
    # spaces at the end of the encrypted message
    print('\n' + ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard
    clip.copy(ciphertext)

def encryptMessage(key, message):
    """
    Encrypts a message using a transposition cipher.
    
    Inputs: key = key with length to transpose letter by.
            message = message to be enciphered.
            
    Outputs: String that is enciphered message by key.
    """
    
    # Each string in the ciphertext represents a column in a grid
    # the grid is length of key, height is length of string / key
    # ciphertext =[''] * key

    # Loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex exceeds message length
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over
            currentIndex += key

    # Convert the ciphertext list into a single string to return
    return ''.join(ciphertext)
    

# If transpositionEncrypt.py is run (not used as a module) call
# the main() function
if __name__ == '__main__':
    main()
