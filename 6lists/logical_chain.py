# ******************
# CALCULADORA LÓGICA
# ******************


def run(values: list, oper: str) -> bool:
    # TU CÓDIGO AQUÍ
    if oper == "and":
        result = all(values)   
    elif oper == "or":
        result = any(values)
    else:
        result = False

    return result


if __name__ == '__main__':
    run([True, True, False], 'and')