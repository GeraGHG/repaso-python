# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
# 

from pathlib import Path

def find_word_occurrences(data_path, target_word):
    with open(data_path, 'r') as file:
        lines = file.readlines()

    matches = []
    target_word = target_word.lower()  # Convertir la palabra objetivo a minúsculas para que coincida sin importar mayúsculas/minúsculas

    for line_number, line in enumerate(lines, start=1):
        line = line.lower()  # Convertir la línea a minúsculas para que coincida sin importar mayúsculas/minúsculas
        words = line.split()
        column_number = 0

        for word in words:
            # Eliminar caracteres especiales al principio o al final de la palabra
            word = word.strip('.,:;()\'¡!-')
            if word == target_word:
                column_number = line.index(word, column_number) + 1  # Encontrar la posición de la palabra
                matches.append((line_number, column_number))

    return matches

if __name__ == '__main__':
    data_path = Path('data/find_words/bzrp.txt')
    target_word = 'persona'
    matches = find_word_occurrences(data_path, target_word)
    new_word = find_word_occurrences(data_path, "me")
    print(matches)
    print(new_word)