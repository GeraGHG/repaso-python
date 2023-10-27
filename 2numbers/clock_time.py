# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    # TU CÓDIGO AQUÍ
    # Hours -> seconds, Minutes -> seconds
    total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
    time_since_midnight = total_seconds * 1000

    return time_since_midnight


if __name__ == '__main__':
    run(0, 1, 1)