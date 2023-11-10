# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    # TU CÓDIGO AQUÍ
    simboly = "█"
    count_letter = {}
    union = []
    with open(data_path, "r") as file:
        text = file.read()
        for letter in text:
            count_letter[letter] = count_letter.get(letter, 0) + 1
    count_letter = dict(sorted(count_letter.items(), key=lambda item: item[0])) # sorted_letters = sorted(letter_counts.items()) también de está forma si solo se ordena la key
    for letter in count_letter:
        union.append(f"{letter} {simboly * count_letter[letter]} {count_letter[letter]}")
    
    with open(histogram_path, "w") as histogra_file:
        #for letter, count in sorted_letters:
            # histogram_line = f'{letter} {"█" * count} {count}\n'
            # output_file.write(histogram_line)
        histogra_file.write("\n".join(union))



    return filecmp.cmp(histogram_path, Path('data\histogram\.expected'), shallow=False)


if __name__ == '__main__':
    path = 'data/histogram/data.txt'
    result = run(path)
    print(result)