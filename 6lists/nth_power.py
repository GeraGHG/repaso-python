# *************
# N ELEVADO A N
# *************


def run(values: list, power: int) -> int:
    # TU CÓDIGO AQUÍ
    if len(values) > power:
        result = values[power] ** power
        return result
    else:
        return -1



if __name__ == '__main__':
    run([1, 2, 3, 4], 2)