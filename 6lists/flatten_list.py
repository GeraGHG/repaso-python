# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    # TU CÓDIGO AQUÍ
    flatten_elements = [item for sublist in elements for item in (run(sublist) if isinstance(sublist, list) else [sublist])]

    return flatten_elements


if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])