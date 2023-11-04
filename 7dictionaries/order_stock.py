# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    # TU CÓDIGO AQUÍ
    if merch in stock:
        if stock[merch] >= amount:
            return True
    return False


if __name__ == '__main__':
    run({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9)