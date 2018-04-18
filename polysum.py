import math
n = 29
s = 1.43256

def polysum(n, s):
    """
    This works out the area + perimeter of a polygon
    n is the number of sides, s is the length of them.
    its round to 4 decimal places. the equation is
    ((0.25 * number of sides * side length ** 2) / tan(pi / number of sides))
    + ((number of sides * side length) ** 2)
    """
    
    sum = round((((0.25) * n * s ** (2))
                 / (math.tan(math.pi / n)) + ((n * s) ** 2)), 4)
    return sum

print(polysum(n, s))
