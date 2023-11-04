# ********************
# CUBOIDES Y VOLÚMENES
# ********************


def run(cuboid1: list, cuboid2: list) -> float:
    # TU CÓDIGO AQUÍ
    mul_cubo1 = 1
    mul_cubo2 = 1
    for side in cuboid1:
        mul_cubo1 *= side
    for side in cuboid2:
        mul_cubo2 *= side
    vol_diff = (mul_cubo1) - (mul_cubo2)
    
    return abs(vol_diff)


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])