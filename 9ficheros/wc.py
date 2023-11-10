# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path

def run(input_path: Path) -> tuple:
    file = open(input_path, "r")
    lines = file.readlines()
    num_lines = len(lines)
    num_words = 0
    num_bytes = 0 
    for linea in lines:
        linea_separada = linea.strip().split(" ")
        num_words += len(linea_separada)
        for word in linea_separada:
            num_bytes += len(word.encode('utf-8')) 
    num_bytes += len(" ".encode('utf-8')) * num_words


    file.close()

    return num_lines, num_words, num_bytes

if __name__ == '__main__':
    # Utiliza Path para crear la ruta absoluta al archivo emojis.txt
    input_file_path = 'data/wc/lorem.txt'
    num_lines, num_words, num_bytes = run(input_file_path)
    print("Number of lines:", num_lines)
    print("Number of words:", num_words)
    print("Number of bytes:", num_bytes)
