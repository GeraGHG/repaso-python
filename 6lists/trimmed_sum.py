# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    if not values:
        return 0  # Si la lista está vacía, la suma es 0

    valor_minimo = min(values)
    valor_maximo = max(values)
    suma = 0
    for elem in values:
        if elem != valor_minimo and elem != valor_maximo:
            suma += elem
    
    return suma


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])