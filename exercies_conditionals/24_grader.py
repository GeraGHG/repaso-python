def grader(num):
    if num > 1 or num < 0.6:
        return "F"
    elif 0.9 <= num:
        return "A"
    elif 0.8 <= num:
        return "B"
    elif 0.7 <= num:
        return "C"
    elif 0.6 <= num:
        return "D"
