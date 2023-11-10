# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path

def sum_matrices(matr1, matr2):
    result = []
    for i in range(len(matr1)):
        row = []
        for j in range(len(matr1[i])):
            row.append(matr1[i][j] + matr2[i][j])
        result.append(row)
    return result



def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = Path('data/sum_matrix/result.dat')
    # TU CÓDIGO AQUÍ
    matrix1 = []
    with open(matrix1_path, "r") as file_matrix1:
        for row in file_matrix1:
            row_split = list(map(int, row.strip().split()))
            matrix1.append(row_split)
    matrix2 = []
    with open(matrix2_path, "r") as file_matrix2:
        for row in file_matrix2:
            row_split = list(map(int, row.strip().split()))
            matrix2.append(row_split)

    sum_matrix = sum_matrices(matrix1, matrix2)
    with open(result_path, "w") as result:
        for line in sum_matrix:
            row = " ".join(str(num) for num in line)
            result.write(row + "\n")
            
    expected_result_path = Path('data/sum_matrix/.expected')
    return filecmp.cmp(result_path, expected_result_path, shallow=False)


if __name__ == '__main__':
    ruta1 = Path('data/sum_matrix/matrix1.dat')
    ruta2 = Path('data/sum_matrix/matrix2.dat')
    resultado = run(ruta1, ruta2)
    print(resultado)


"""
Preguntar a chatgpt otra forma utilizó la biblioteca de numpy
import numpy as np
import filecmp
from pathlib import Path

def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = Path('data/sum_matrix/result.dat')

    matrix1 = np.loadtxt(matrix1_path)
    matrix2 = np.loadtxt(matrix2_path)

    if matrix1.shape != matrix2.shape:
        print("Las matrices no tienen el mismo tamaño y no se pueden sumar.")
        return False

    sum_matrix = matrix1 + matrix2

    np.savetxt(result_path, sum_matrix, fmt='%d', delimiter=' ')

    expected_result_path = Path('data/sum_matrix/.expected')

    return filecmp.cmp(result_path, expected_result_path, shallow=False)

if __name__ == '__main__':
    resultado = run(Path('data/sum_matrix/matrix1.dat'), Path('data/sum_matrix/matrix2.dat'))
    print(resultado)


"""