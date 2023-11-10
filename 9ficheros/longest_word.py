# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    # TU CÓDIGO AQUÍ
    longest_word = ""
    with open(input_path, "r") as file:
        text = file.read()
        words = text.split()
        for word in words:
            word = word.strip(",.;:()")
            if len(word) > len(longest_word):
                longest_word = word
            

    return longest_word


if __name__ == '__main__':
    file = Path("data/longest_word/python.txt")
    result = run(file)
    print(result)