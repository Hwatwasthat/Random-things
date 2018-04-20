<<<<<<< HEAD
from fractions import gcd
from functools import reduce

def lcm(a, b):
    "Get the lowest common multiple of two integers a and b"
    return a * b // gcd(a, b)

"""
reduce gets the list, in this case the numbers 1 - 20, and applies the function
that is input in the first argument to them all in order (e.g (((1 + 2) + 3) + 4)
and returns the outcome of this
"""
result = reduce(lcm, range(1, 4))
print(result)
=======
from fractions import gcd
from functools import reduce

def lcm(a, b):
    "Get the lowest common multiple of two integers a and b"
    return a * b // gcd(a, b)

"""
reduce gets the list, in this case the numbers 1 - 20, and applies the function
that is input in the first argument to them all in order (e.g (((1 + 2) + 3) + 4)
and returns the outcome of this
"""
result = reduce(lcm, range(1, 4))
print(result)
>>>>>>> 7e1264f782abda423dc21c11e901e4507678a674
