objetivo_x = 7
objetivo_y = 8
x = 0
y = 0
while x != objetivo_x or y != objetivo_y:
    if not(y < x) or (x == y):
        print(f"({x, y})")
    if x == y:
        x += 1
    elif y <= x:
        y += 2
    elif x < y:
        x += 2
    elif y > x:
        y += 1

