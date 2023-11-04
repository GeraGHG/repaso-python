# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    # TU CÓDIGO AQUÍ
    sum_positive = sum(num for num in numbers if num > 0)

    return sum_positive


if __name__ == '__main__':
    run([1, -4, 7, 12])