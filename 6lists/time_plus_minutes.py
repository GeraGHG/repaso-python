# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    # TU CÓDIGO AQUÍ
    hours, minutes = time.split(":")
    sum_minutes = int(minutes) + offset
    hour, residuo = divmod(sum_minutes, 60)
    suma_horas = int(hours) + hour
    if suma_horas >= 24:
        hours =  abs(24 - (int(hours) + hour))
        return f"{hours}:{residuo}"
    final_time = f"{suma_horas}:{residuo}"

    return final_time


if __name__ == '__main__':
    run('17:15', 240)