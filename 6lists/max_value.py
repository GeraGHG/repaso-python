# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    mayor = -100
    for num in values:
        if num > mayor:
            mayor = num
    max_value = mayor

    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])