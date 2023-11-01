week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
dict_day = {i + 1: day for i, day in enumerate(week)}

try:
    choose = int(input("Enter a number: "))
    if 1 <= choose <= 7:
        print(dict_day[choose])
    else:
        print("Wrong, please enter a number between 1 and 7")
except ValueError:
    print("Invalid input. Please enter a valid number.")
