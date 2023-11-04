# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    # TU CÓDIGO AQUÍ
    add_inv = sum(numbers) * (-1)

    return add_inv


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])