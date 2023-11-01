def pump(miles, gallons_left):
    car_per_gallon = 25
    if car_per_gallon * gallons_left >= miles:
        return True
    elif car_per_gallon * gallons_left < miles:
        return False
print(pump(50, 2))