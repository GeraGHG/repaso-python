# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    # TU CÓDIGO AQUÍ
    # Calcula la circunferencia a partir de la longitud del arco A
    circunferencia = arc_A * 4

    # Calcula el lado del cuadrado
    lado = circunferencia / 4

    # Calcula el área del cuadrado
    area = 3.14 * lado**2

    # Redondea el resultado a 10 cifras decimales
    area = round(area, 10)
    return area


if __name__ == '__main__':
    run(1)