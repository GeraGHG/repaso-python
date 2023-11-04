# *********************
# CADA NOTA EN SU SITIO
# *********************


def run(marks: dict) -> tuple:
    # TU CÓDIGO AQUÍ
    passed = {nombre.upper(): nota for nombre, nota in marks.items() if nota >= 5}
    failed = {nombre.lower(): nota for nombre, nota in marks.items() if nota < 5}

    return passed, failed


if __name__ == '__main__':
    run({'Ana': 4, 'Domingo': 7, 'Eva': 5, 'Álvaro': 3, 'Juan': 8, 'Belén': 1})