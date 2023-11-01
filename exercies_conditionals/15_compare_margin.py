def close_compare(a, b, margin=0):
    diff = abs(a - b)
    if diff <= margin:
        return 0
    elif diff > margin and a < b:
        return -1
    elif diff > margin and a > b:
        return 1