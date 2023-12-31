# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict: # return {city: int(population.replace("_", "")) for city, population in [item.split(":") for item in cinfo.split(";")]}
    # TU CÓDIGO AQUÍ
    cities_population = cinfo.split(";")

    cities = {}
    for item in cities_population:
        city, population = item.split(":")
        cities[city] = int(population)

    return cities


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')