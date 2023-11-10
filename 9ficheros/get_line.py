# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    # TU CÓDIGO AQUÍ
    with open(input_path, "r") as file_findline:
        rows = file_findline.readlines()
        for i, row in enumerate(rows, start=1):
            if line_no == i:
                return row
        return None


if __name__ == '__main__':
    route = Path("data/get_line/nasdaq.txt")
    result = run(route, 10)
    print(result)