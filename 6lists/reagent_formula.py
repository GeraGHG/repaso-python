# ************
# ELLA QUÍMICA
# ************


def run(formula: list) -> bool:
    # TU CÓDIGO AQUÍ
    if 1 in formula and 2 in formula:
        return False

    # Regla 2: El componente 3 y el componente 4 no se pueden seleccionar al mismo tiempo.
    if 3 in formula and 4 in formula:
        return False

    # Regla 3: El componente 5 y el componente 6 tienen que seleccionarse al mismo tiempo.
    if (5 in formula and 6 not in formula) or (5 not in formula and 6 in formula):
        return False

    # Regla 4: El componente 7 o el componente 8 tienen que seleccionarse (uno de los dos, o los dos).
    if 7 not in formula and 8 not in formula:
        return False

    # Si no se violó ninguna regla, la fórmula es válida.
    return True

if __name__ == '__main__':
    run([1, 3, 7])