# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    # TU CÓDIGO AQUÍ
    data = []
    with open(datafile, "r") as file:
        lines = file.readlines()
        header = lines[0].strip().split(",")

        for line in lines[1:]:
            values = line.strip().split(",")
            record = {}

            for i in range(len(header)):
                key = header[i]
                value = values[i] 

                if value == "True":
                    record[key] = True
                elif value == "False":
                    record[key] = False
                elif value.isdigit():
                    record[key] = int(value)
                else:
                    record[key] = value
            data.append(record)

    return data


if __name__ == '__main__':
    datafile = Path('data/read_csv/pokemon.csv')
    data = run(datafile)
    print(data)