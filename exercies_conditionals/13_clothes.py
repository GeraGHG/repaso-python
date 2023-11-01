def washing_machine(water, load, amount_clothes):
    if amount_clothes > (load * 2):
        return "Too much clothes"
    elif amount_clothes < load:
        return "Not enough clothes"
    else:
        required_water = water * 1.1**(amount_clothes - load)
        return round(required_water, 2)
        
print(washing_machine(5, 10, 14))