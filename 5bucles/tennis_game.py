# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    # TU CÓDIGO AQUÍ
    points_A = points.count("A")
    points_B = points.count("B")
    winner = "A" if points_A > points_B else "B" if points_B > points_A else "AB"

    return winner


if __name__ == '__main__':
    run('ABAABA')