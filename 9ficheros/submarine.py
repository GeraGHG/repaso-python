# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:
    # TU CÓDIGO AQUÍ
    distance = depth = fuel = 0

    x = 0
    y = 0
    consumo_x = 3
    consumo_y = 2
    subir = 0
    bajar = 600
    with open(route_path, "r") as file_submarine:
        combustible = int(file_submarine.readline())
        cordenadas = file_submarine.readline().split(",")

        for cordenada in cordenadas:
            cor_x, cor_y = map(int, cordenada.split(":"))
            combustible -= ((abs(cor_x) * consumo_x) + (abs(cor_y) * consumo_y))
            x += cor_x
            y += cor_y
            if combustible <= 0 or y < subir or y > bajar:
                break
    distance = x
    depth = y
    fuel = combustible
    return distance, depth, fuel


if __name__ == '__main__':
    path = 'data/submarine/route1.dat'
    result = run(path)
    print(result)