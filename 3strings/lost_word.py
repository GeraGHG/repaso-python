# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    # TU CÓDIGO AQUÍ
    index = text.find(target_word)
    firts_part_text = text[:index]
    range_word = len(target_word)
    second_part_text = text[index+range_word:]

    mtext = firts_part_text + replace_word + second_part_text

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')