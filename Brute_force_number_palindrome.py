<<<<<<< HEAD
def number_palindrome():
    output = 0
    # Iterate through 100 - 1000 on both variables
    for i in range (100, 1000):
        for x in range (100, 1000):

            # Work out the product of the two and then reverse
            # using a string conversion
            c = i * x
            cc = str(c)
            cr = cc[::-1]

            # Check if the strings are palindromes, therefore
            # the numbers are, and that this is the largest
            # palindrome encountered so far
            if cc == cr and c > output:
                output = c

    return output

print(number_palindrome())
                
=======
def number_palindrome():
    output = 0
    # Iterate through 100 - 1000 on both variables
    for i in range (100, 1000):
        for x in range (100, 1000):

            # Work out the product of the two and then reverse
            # using a string conversion
            c = i * x
            cc = str(c)
            cr = cc[::-1]

            # Check if the strings are palindromes, therefore
            # the numbers are, and that this is the largest
            # palindrome encountered so far
            if cc == cr and c > output:
                output = c

    return output

print(number_palindrome())
                
>>>>>>> 7e1264f782abda423dc21c11e901e4507678a674
