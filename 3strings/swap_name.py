# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    # TU CÓDIGO AQUÍ
    first_name, last_name = fullname.split(" ", 1)
    swapname = f"{last_name} {first_name}"

    return swapname


if __name__ == '__main__':
    run('John McClane')