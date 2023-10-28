# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    # TU CÓDIGO AQUÍ
    count_vowels = sum(1 for letter in text if letter in "aeiou")
    metric = len(text) * count_vowels

    return metric


if __name__ == '__main__':
    run('ordenador')