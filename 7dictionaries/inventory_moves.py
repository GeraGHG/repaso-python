# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    # TU CÓDIGO AQUÍ
    inventory = {}
    create = imoves.split(",")
    for item in create:
        key, value = item[0], int(item[1:])
        if key in inventory:
            inventory[key] += value
        else:
            inventory[key] = value
    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')