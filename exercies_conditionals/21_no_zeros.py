def no_zeros(num):
    num_str = str(num)
    num_str = num_str.rstrip("0")
    return int(num_str)
print(no_zeros(1450))
print(no_zeros("1050"))
print(no_zeros(-1050))