# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
    # TU CÓDIGO AQUÍ
    coef, exp = symbol.split(",")
    new_coef, new_exp = int(coef) / (int(exp) + 1), int(exp) + 1
    integral = f"{int(new_coef)}x^{int(new_exp)}"

    return integral


if __name__ == '__main__':
    run('3,2')