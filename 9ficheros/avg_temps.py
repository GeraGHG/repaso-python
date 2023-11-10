# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'C:/users/Germanico/Documents/python_repaso/9ficheros/data/avg_temps/avg_temps.dat'
    # TU CÓDIGO AQUÍ
    # Leer el archivo de entrada
    with open(input_path, 'r') as input_file:
        data = input_file.readlines()

    avg_temperatures = []

    # Calcular la temperatura media de cada mes
    for d in data:
        temperatures = map(int, d.split())
        avg_temperature = sum(temperatures) / len(temperatures)
        avg_temperatures.append(f"{avg_temperature:.2f}")

    # Escribir el archivo de salida con las temperaturas medias
    with open(output_path, 'w') as output_file:
        output_file.write('\n'.join(avg_temperatures))

    return filecmp.cmp(output_path, Path('C:/Users/Germanico/Documents/python_repaso/9ficheros/data/avg_temps/.expected'), shallow=False)


if __name__ == '__main__':
    run('C:/Users/Germanico/Documents/python_repaso/9ficheros/data/avg_temps/temperatures.dat')