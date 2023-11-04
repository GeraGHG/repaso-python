# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    # TU CÓDIGO AQUÍ
    total_population = sum(map(int, pdata.values()))
    avg_data = {}
    for city_population in pdata:
        avg_data[city_population] = round(pdata[city_population] * 100 / total_population, 3)

    return avg_data


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})