import math
def nearest_sq(n):
    root = int(math.sqrt(n))
    if math.sqrt(n) == root:
        return n
    lower_squaret = root ** 2
    higher_squaret = (root + 1) ** 2

    if abs(n - lower_squaret) <= abs(n - higher_squaret):
        return lower_squaret
    else:
        return higher_squaret
    
print(nearest_sq(111))
