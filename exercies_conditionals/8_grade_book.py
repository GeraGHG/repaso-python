def grade_book(value1, value2, value3):
    score = (value1 + value2 + value3) / 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 0 <= score <= 59:
        return "F"
    else:
        return "Enter values positives please!"
print(grade_book(70, 89, 68))
