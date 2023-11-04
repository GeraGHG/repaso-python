lista_nums = []
for i in range(1, 10):
    num = "1"
    lista_nums.append(f"{num*i}.{num*i}")

leng_list = len(lista_nums)
mayor = len(lista_nums[-1])
for i in range(leng_list):
    num_add = mayor - len(lista_nums[i])
    print(" " * (num_add//2) + lista_nums[i])

