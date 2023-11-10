# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    # TU CÓDIGO AQUÍ
    with open(input_path, "r") as file:
        words_dict = {}
        text = file.read()
        spaces_words = text.split()
        for word in spaces_words:
            word = word.strip(".;,():").lower()
            words_dict[word] = words_dict.get(word, 0) + 1
    # order = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
    freq = {}
    for key, value in words_dict.items():
        if value >= lower_bound:
            freq[key] = value

    return freq


if __name__ == '__main__':
    root = Path('data/word_freq/cistercian.txt')
    result = run(root, 8)
    print(result)