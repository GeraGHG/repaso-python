# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    # TU CÓDIGO AQUÍ
    to_bin = bin(num)

    return to_bin.lstrip("0b")


if __name__ == '__main__':
    run(1)