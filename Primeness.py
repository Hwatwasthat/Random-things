from math import sqrt
from itertools import count, islice

def primeness(n):
    """
    Takes the input, checks its larger than 1 and then returns true if the number is not divisible
    by a number in an iterative counter between 2 and the integered square root of itself.
    islice(count) operates on the basis of iterating from the first argument (2 in this case)
    as many times as stated in the second argument. A third argument can change the step size,
    which defaults to 1.
    """
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

  
def main():
    num_prime = 0
    i = 1

    while num_prime < 10001:
        i += 1
        if primeness(i) == 1:
            num_prime += 1

    print(i)
  
main()
