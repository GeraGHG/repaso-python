def sum_mul(n, m):
    if m < 1 or n > m:
        return "INVALID"
    list_nums = []
    for i in range(2, m):
        if i % n == 0:
            list_nums.append(i)
    str_answer = " + ".join(map(str, list_nums)) + f" = {sum(list_nums)}"
    return str_answer
print(sum_mul(2, 9))
