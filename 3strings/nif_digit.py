# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************

def run(nif: str) -> str:
    # TU CÓDIGO AQUÍ
    letras_control = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(nif) == 8:
        num_int = int(nif)
        wnif = letras_control[num_int % 3]
        return wnif

if __name__ == '__main__':
    run('78654355')