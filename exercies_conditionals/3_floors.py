def floor_to_europ(floor):
    if floor <= 0:
        return f"{floor} => {floor}"
    elif 1 <= floor <= 12:
        return f"{floor} => {floor - 1}"
    elif floor == 13:
        return f"No exits this floor"
    elif 14 <= floor < 1000:
        return f"{floor} => {floor - 2}"
print(floor_to_europ(15))
        