# ******************
# AGRUPANDO PALABRAS
# ******************

def group(inital, words: list):
    initial_group = []
    for word in words:
        if word[0] == inital:
            initial_group.append(word)
    return initial_group


def run(words: list) -> dict:
    # TU CÓDIGO AQUÍ
    group_words = {}
    for w in words:
        letter = w[0]
        if letter not in group_words:
            group_words[letter] = group(letter, words)
            
    return group_words


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])