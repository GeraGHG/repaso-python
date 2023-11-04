# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    # TU CÓDIGO AQUÍ
    available_currencies.sort(reverse=True)
    residuo = to_give_back
    change = {}

    for bil_money in available_currencies:
        while residuo >= bil_money:
            change[bil_money] = change.get(bil_money, 0) + 1
            residuo -= bil_money
    if residuo == 0:
        return change

if __name__ == '__main__':
    run(20, [5, 2, 1])