def evil_or_odiou(num):
    num_bin = bin(num) # remeber bin() -> return str
    count_ones = num_bin.count("1")
    if count_ones % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"