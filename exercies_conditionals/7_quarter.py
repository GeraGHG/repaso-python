def num_month(num: int):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    quarters = {i: "first" if 1 <= i <= 4 else "second" if 5 <= i <= 8 else "third" for i in range(1, 13)}

    if 1 <= num <= 12:
        return f"Month {num} ({months[num-1]}), is part of the {quarters[num]} quarter"
print(num_month(5))