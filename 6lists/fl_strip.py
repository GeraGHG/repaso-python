# ****************
# TROCEADO EXTREMO
# ****************


def run(numbers: str) -> str:
    # TU CÓDIGO AQUÍ
    nums_split = numbers.split(",")
    if not (len(nums_split) > 2):
        return ""
    del nums_split[0]
    del nums_split[-1]
    strip_numbers = " ".join(nums_split)
    return strip_numbers


if __name__ == '__main__':
    run('1,2,3')