# **************************
# BARICENTRO DE UN TRIÁNGULO
# **************************


def run(A: list, B: list, C: list) -> tuple:
    # TU CÓDIGO AQUÍ

    xA, xB, xC = A[0], B[0], C[0]
    yA, yB, yC = A[1], B[1], C[1]

    x0 = round((xA + xB + xC) / 3, 4)
    y0 = round((yA + yB + yC) /3, 4)
    return x0, y0


if __name__ == '__main__':
    run([4, 6], [12, 4], [10, 10])