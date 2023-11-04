# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    # TU CÓDIGO AQUÍ
    nums_consecutive = []
    num_diferent = None
    for num in items:
        if num != num_diferent:
            num_diferent = num
            nums_consecutive.append(num)

    result = nums_consecutive

    return result


if __name__ == '__main__':
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])