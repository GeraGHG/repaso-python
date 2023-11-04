# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    # TU CÓDIGO AQUÍ
    if to_give_back == 0:
        return {}
    orded_currencies = dict(sorted(available_currencies.items(), key=lambda item: item[0], reverse=True))
    money_back = {}
    for money in orded_currencies:
        mount = orded_currencies[money]
        while to_give_back >= money and mount > 0:
            money_back[money] = money_back.get(money, 0) + 1
            mount -= 1
            to_give_back -= money
    if to_give_back == 0:
        return money_back
    else:
        return None


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})