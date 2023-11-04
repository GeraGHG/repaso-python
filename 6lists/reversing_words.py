# *************************
# PALABRAS EN ORDEN INVERSO
# *************************


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    new_text = text.lower().split(" ")
    reversing = " ".join(new_text[::-1])

    return reversing


if __name__ == '__main__':
    run('Hello World')