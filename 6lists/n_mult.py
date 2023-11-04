# ********************
# CALCULANDO MÚLTIPLOS
# ********************


def run(x: int, n: int) -> list:
    # TU CÓDIGO AQUÍ
    multiples = [num for num in range(x, x*n + 1, x) if num <= x*n]

    return multiples


if __name__ == '__main__':
    run(1, 10)