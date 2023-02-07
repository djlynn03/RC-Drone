import math

def angle(x, y):
    if x == 0:
        return 0
    return math.degrees(math.atan(y / x))
