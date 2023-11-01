def count_total(days_car):
    cost_per_day = 40
    total_off_3 = 20
    total_off_7 = 50
    if days_car >= 7:
        return days_car * cost_per_day - total_off_7
    elif days_car >= 3:
        return days_car * cost_per_day - total_off_3
    

