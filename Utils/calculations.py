import math

def normalize(x, y):
    """Returns the normalized joystick position"""
    xyMagnitude = math.sqrt(x**2 + y**2)
    if xyMagnitude > 1:
        return x / xyMagnitude, y / xyMagnitude
    else:
        return x, y

def angleDegrees(x, y):
    """Returns the angle of the joystick position according to the unit circle in degrees"""
    x, y = normalize(x, y)
    degrees = -math.degrees(math.atan2(y, x))
    if degrees >= 0:
        return abs(degrees)
    else:
        return 360 + degrees

def magnitude(x, y):
    """Returns the magnitude of the joystick position as a percentage of the maximum magnitude"""
    x, y = normalize(x, y)
    return math.sqrt(x**2 + y**2)
