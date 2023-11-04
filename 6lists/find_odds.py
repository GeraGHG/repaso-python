# ********************
# DESCUBRIENDO IMPARES
# ********************


def run(values: list) -> list:
    # TU CÓDIGO AQUÍ
    uniques = list(set(values))
    uniques.sort()
    return [num for num in uniques if num % 2 != 0]

if __name__ == '__main__':
    run([1, 2, 3, 4, 5])