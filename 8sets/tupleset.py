# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:
    # TU CÓDIGO AQUÍ
    par1 = {tup[0] for tup in input}
    par2 = {tup[1] for tup in input}
    # part1 = set()
    # part2 = set()
    # output = (part1, part2)
    # for tup in input:
    #     part1.add(tup[0])
    #     part2.add(tup[1])
    return par1, par2


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))