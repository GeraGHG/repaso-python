# *********************
# VALOR MÁXIMO Y MÍNIMO
# *********************


def run(values: list) -> tuple:
    # TU CÓDIGO AQUÍ
    max_value = -1000
    min_value = 1000
    for num in values:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return max_value, min_value


if __name__ == '__main__':
    run([4, 6, 2, 1, 9, 63, -134, 566])