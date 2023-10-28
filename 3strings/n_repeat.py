# *************
# SUMA REPETIDA
# *************


def run(n: int) -> int:
    # TU CÓDIGO AQUÍ
    n_str = str(n)
    result = n + int(n_str * 2) + int(n_str * 3)

    return result


if __name__ == '__main__':
    run(3)