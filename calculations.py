import math

def angle(x, y):
    if x == 0:
        return 0
    return math.degree(math.atan(y / x))