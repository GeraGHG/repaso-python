# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************


def run(year: int) -> int:
    # TU CÓDIGO AQUÍ
    list_range_centuries = []
    num_range = 1
    if year > 2000:
        return 21
    for _ in range(21):
        list_range_centuries.append(num_range)
        num_range += 100
    
    for posicion in range(len(list_range_centuries) - 1):
        if list_range_centuries[posicion] <= year < list_range_centuries[posicion + 1]:
            century = posicion + 1
            return century


if __name__ == '__main__':
    run(1705)