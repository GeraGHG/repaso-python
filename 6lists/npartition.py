# ***********************
# PARTICIÓN POR EL NÚMERO
# ***********************


def run(values: list, ref_value: int) -> list:
    # TU CÓDIGO AQUÍ
    low = []
    up = []
    for value in values:
        if value < ref_value:
            low.append(value)
        else:
            up.append(value)

    npartition = [low, up]

    return npartition


if __name__ == '__main__':
    run([4, 3, 2, 9, 8, 5], 4)