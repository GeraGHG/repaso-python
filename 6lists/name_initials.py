# **********************
# INICIALES DE UN NOMBRE
# **********************

import string
def run(fullname: str) -> str:
    # TU CÓDIGO AQUÍ
    word_upper = string.ascii_uppercase
    last_names, name = fullname.split(",")
    last_names = last_names.title()
    name = name.title()
    initials = ""
    for letter in name:
        if letter in word_upper:
            initials = letter + "." + initials
            break
    for letter in last_names:
        if letter in word_upper:
            initials += (letter + ".")
    
    return initials


if __name__ == '__main__':
    run('Delgado Quintero, sergio')