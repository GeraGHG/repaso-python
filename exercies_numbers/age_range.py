def range_age(age):
    if age == 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
        return f"age = {age}  =>  {min}-{max}"
    return f"age = {age} => {int(age/2 + 7)}-{(age-7) * 2}"