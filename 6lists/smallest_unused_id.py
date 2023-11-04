# *****************
# MENOR ID SIN USAR
# *****************


def run(ids: list) -> int:
    # TU CÓDIGO AQUÍ
    smallest_unused_id = 'output'
    ids.sort()
    smallest_unused_id = 1
    for num in ids:
        if num == smallest_unused_id:
            smallest_unused_id += 1
    
    return smallest_unused_id

if __name__ == '__main__':
    run([3, 1, 8, 4, 9])