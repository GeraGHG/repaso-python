# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    output_path = Path('data/replace_chars/r_noticia.txt')
    # TU CÓDIGO AQUÍ
    letters = replacements.split("|")
    check = {letter[0]: letter[1] for letter in letters}

    text_union = []
    with open(input_path, "r") as file:
        text_line = file.readlines()
        for paragraph  in text_line:
            one_paragra = ""
            for letter in paragraph:import filecmp
from pathlib import Path

def run(input_path: Path, replacements: str) -> bool:
    output_path = Path('data/replace_chars/r_noticia.txt')
    # TU CÓDIGO AQUÍ
    letters = replacements.split("|")
    check = {letter[0]: letter[1] for letter in letters}

    text_union = []
    with open(input_path, "r") as file:
        text_line = file.readlines()
        for paragraph in text_line:
            one_paragra = ""
            for letter in paragraph:
                if letter in check:
                    one_paragra += check[letter]
                else:
                    one_paragra += letter
            text_union.append(one_paragra)
    
    with open(output_path, "w") as file:
        file.write("\n".join(text_union))
    
    return filecmp.cmp(output_path, Path('data/replace_chars/.expected'), shallow=False)

if __name__ == '__main__':
    path = Path('data/replace_chars/noticia.txt')
    result = run(path, 'áa|ée|íi|óo|úu')
    print(result)

                if letter in check:
                    one_paragra += check[letter]
                else:
                    one_paragra += letter
            text_union.append(one_paragra)
    with open(output_path, "w") as file:
        file.write("\n".join(text_union))
    return filecmp.cmp(output_path, Path('data\replace_chars\.expected'), shallow=False)


if __name__ == '__main__':
    path = 'data/replace_chars/noticia.txt'
    result = run(path, 'áa|ée|íi|óo|úu')
    print(result)