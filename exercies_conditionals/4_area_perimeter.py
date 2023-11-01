def polygon(length, width):
    if length == width:
        return length * width
    else:
        return length*2 + width*2

print(polygon(3, 3))
