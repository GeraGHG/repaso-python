# *************************
# QUITANDO PRIMERO Y ÚLTIMO
# *************************


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    first_letter = text[0]
    last_letter = text[-1]
    stext = text.lstrip(first_letter).rstrip(last_letter)
    return stext


if __name__ == '__main__':
    run('What can I do')