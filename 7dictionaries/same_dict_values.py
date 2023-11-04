# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    # TU CÓDIGO AQUÍ
    if not items:
        return True
    dates = list(items.values())
    first_value = dates[0] 
    return all(first_value == value for value in dates)


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})