# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    # TU CÓDIGO AQUÍ
    number = str(number)

    rev_digits = list(map(int, [n for n in number[::-1]]))
    return rev_digits

if __name__ == '__main__':
    run(35231)