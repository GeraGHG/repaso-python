# *************************
# LA MULTIPLICACIÓN DE JACK
# *************************


def run(n: int) -> int:
    # TU CÓDIGO AQUÍ
    if n > 0:
        result = n * 5**int(len(str(n)))
    else:
        num_str = str(n)
        num_str = num_str[1:]
        result = n * 5**int(len(num_str))

    return result


if __name__ == '__main__':
    run(3)