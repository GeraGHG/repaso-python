# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    # TU CÓDIGO AQUÍ
    num_comprobacion = items[0]
    all_same = all(num_comprobacion == num for num in items)

    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])