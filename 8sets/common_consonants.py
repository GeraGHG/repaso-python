# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    # TU CÓDIGO AQUÍ
    new_text1 = text1.lower().replace(" ", "").strip()
    print(new_text1)
    new_text2 = text2.lower().replace(" ", "").strip()
    print(new_text2)
    only_text1 = ""
    only_text2 = ""
    for letter in new_text1:
        if letter not in "aeiou":
            only_text1 += letter
    for letter in new_text2:
        if letter not in "aeiou":
            only_text2 += letter
        

    return "".join(sorted(set(only_text1) & set(only_text2)))


if __name__ == '__main__':
    run('Flat is bEtter than nested', 'Readability counts')