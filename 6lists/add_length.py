# *********************
# PALABRAS CON LONGITUD
# *********************


def run(text: str) -> list:
    # TU CÓDIGO AQUÍ
    text_split = text.split(" ")
    words_length = []
    for word in text_split:
        length = len(word)
        union = f"{word} {length}"
        words_length.append(union)
    return words_length


if __name__ == '__main__':
    run('todo se transforma')