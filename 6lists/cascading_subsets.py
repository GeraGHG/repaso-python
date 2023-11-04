# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    # TU CÓDIGO AQUÍ
    cascading = 'output'
    subconjuntos = []
    for i in range(len(values) - size + 1):
        subconjunto = []
        for j in range(i, i + size):
            subconjunto.append(values[j])
        subconjuntos.append(subconjunto)

    return subconjuntos


if __name__ == '__main__':
    run([1, 2, 3, 4], 3)