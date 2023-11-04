# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    # TU CÓDIGO AQUÍ
    chars = [char for char in "".join(texts)]


    return chars


if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])