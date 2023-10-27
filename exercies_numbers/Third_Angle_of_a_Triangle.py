
def third_angle(angleA, angleB):
    if angleA + angleB < 180:
        return "The third angle is: ", 180 - (angleA + angleB)
    return "It's not a triangle"

print(third_angle(75, 45))