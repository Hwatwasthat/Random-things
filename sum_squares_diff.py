test = int(input("What do you want to get the squared sum - the sum squared of?:"))
           
def sum_squares(top):
    "Returns the squares of the numbers between 1 and top inclusive added together"
    sums = 0

    for i in range(1, top + 1):
        sums += i ** 2

    return sums

def sums2(top):
    "Returns the numbers between 1 and top inclusive added together and then squared"
    sums = 0

    for i in range(1, top + 1):
        sums += i

    return sums ** 2
    

def main(top):
    """
    Compares the differenced between the numbers 1 and a + 1 when they are added then squared
    and when they are sqaured then added.
    """
    diff = sums2(top) - sum_squares(top)
    return diff

result = (main(test))

print(f"\nThe difference between the values is {result}")
