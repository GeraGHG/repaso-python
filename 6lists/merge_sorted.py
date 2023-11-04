# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    # TU CÓDIGO AQUÍ
    merged = []
    i, j = 0, 0
    while i < len(values1) and j < len(values2):
        if values1[i] < values2[j]:
            merged.append(values1[i]) 
            i += 1
        elif values1[i] > values2[j]:
            merged.append(values2[j])
            j += 1
        else:
            merged.append(values1[i])
            i += 1
            j += 1
    merged.extend(values1[i:])
    merged.extend(values2[j:])
    # Eliminar duplicados manteniendo el orden
    merged = list(dict.fromkeys(merged))
    return merged


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])

