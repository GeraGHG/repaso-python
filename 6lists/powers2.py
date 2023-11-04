# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    # TU CÓDIGO AQUÍ
    if num_powers == 0:
        return [1]
    powers2 = [2**i for i in range(num_powers + 1)]

    return powers2


if __name__ == '__main__':
    run(0)